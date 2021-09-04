import sys
# PyQt related library
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore
# request related library
import requests
import json
import base64
import os
import logging
import speech_recognition as sr
import csv
# nlp library
import jieba
# load local dictionary
jieba.load_userdict("./nlp_dic/dic.txt")
import jieba.posseg
import jieba.analyse

class EHR_Ctr(QMainWindow):
	def setCtr(self, EHR_View):
		self.EHR_View = EHR_View
		self.connectSlot()

	# bind functions and buttons
	def connectSlot(self):
		self.EHR_View.record_Signal.connect(self.record)
		self.EHR_View.quit_Signal.connect(self.quit)
		self.EHR_View.select_Signal.connect(self.select_file)
		self.EHR_View.save_Signal.connect(self.save_file)

	# start recording and show message in statusbar
	def record(self): 
		self.EHR_View.statusBar().showMessage('Recording...')
		self.record_audio()
	
	# quit the application
	# used for test for now
	def quit(self): 
		text = '病人名字：张三李四，年龄35岁，号码20031525，就诊时间2020年2月10日16点。症状为：咳嗽和发烧。诊断为感冒或者发烧。建议吃感冒药，比如感冒灵。'
		self.token(text)
		# sys.exit(0)

	# select a local .wav file to do voice recognition and fill in
	def select_file(self):
		print("select file")
		dir = QFileDialog.getOpenFileName(self, "选择文件", "/", "Wav Files (*.wav)")
		# error handle: ensure valid input
		if dir[0] != '':
			target = self.audio_baidu(dir[0])
			self.token(target[0])

	# save the EHR form into csv file
	def save_file(self):
		# categories
		Patient_Name = self.EHR_View.plainTextEdit_Name.toPlainText()
		Patient_ID = self.EHR_View.plainTextEdit_ID.toPlainText()
		Date = self.EHR_View.plainTextEdit_Date.toPlainText()
		Sympotom = self.EHR_View.plainTextEdit_Sympotom.toPlainText()
		Disease = self.EHR_View.plainTextEdit_Disease.toPlainText()
		Treatment = self.EHR_View.plainTextEdit_Treatment.toPlainText()
		WholeText = self.EHR_View.plainTextEdit_WholeText.toPlainText()
		# direction to save
		save_dir = QFileDialog.getSaveFileName(self, 
			"getSaveFileName","./",
			"Csv Files (*.csv)")
		# error handle: ensure valid input
		if save_dir[0] != '':
			# two rows 'Prop' and 'Info'
			headers = ['Prop','Info']
			# ('Prop','Info')
			rows = [('Patient Name', Patient_Name),
					('Patient ID', Patient_ID),
					("Date", Date),
					("Sympotom", Sympotom),
					("Disease", Disease),
					("Treatment", Treatment),
					("WholeText", WholeText)]
			# write into the file
			with open(save_dir[0],'w') as f:
				f_csv = csv.writer(f)
				f_csv.writerow(headers)
				f_csv.writerows(rows)

	# get token from baidu server
	def get_token(self):
		logging.info('开始获取token...')
		# linking attributes
		baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
		grant_type = "client_credentials"
		client_id = "vXSGRTBflzpKFqMOKIqbfMb6"
		client_secret = "vQlsg2vPRsHdtS6WQ75mNtLMgrGQEBLu"
		# get url
		url = f"{baidu_server}grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}"
		res = requests.post(url)
		token = json.loads(res.text)["access_token"]
		return token

	# connect to the server and recognize
	def audio_baidu(self,filename):
		#start to recognize the voice file
		logging.info('开始识别语音文件...')
		# open the file
		with open(filename, "rb") as f:
			speech = base64.b64encode(f.read()).decode('utf-8')
		size = os.path.getsize(filename)
		token = self.get_token()
		headers = {'Content-Type': 'application/json'}
		url = "https://vop.baidu.com/server_api"
		data = {
			"format": "wav",
			"rate": "16000",
			# 1537 for chinese, 1737 for english
			"dev_pid": "1537",
			#"lan": "en",
			"speech": speech,
			"cuid": "dc:a9:04:72:13:4b",
			"len": size,
			"channel": 1,
			"token": token,
		}
		# pull request
		req = requests.post(url, json.dumps(data), headers)
		result = json.loads(req.text)
		# check return values
		if result["err_msg"] == "success.":
			print(result['result'])
			self.EHR_View.statusBar().showMessage('finished!')
			return result['result']
		# failed to recognize the voice file
		else:
			print("Failed to recognize the content!")
			return -1

	# record audio file in .wav
	def record_audio(self):
		logging.basicConfig(level=logging.INFO)
		wav_num = 0
		# initialize a speech_recognition
		r = sr.Recognizer()
		# open the micro
		mic = sr.Microphone()
		logging.info('recording...')
		with mic as source:
			# noise reduction
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
		with open(f"./records/00{wav_num}.wav", "wb") as f:
			# save into wav file
			f.write(audio.get_wav_data(convert_rate=16000))
		logging.info('Recording has been done，start recognizing...')
		target = self.audio_baidu(f"./records/00{wav_num}.wav")
		# target[0] is the whole recognized content 
		self.token(target[0])

	# analyse the content and fill into corresponding cells
	def token(self,text):
		# fill the whole recognized content into the "WholeText"
		self.EHR_View.plainTextEdit_WholeText.setPlainText(text)
		# nlp
		normal_list = []
		paddle_list = []
		print('Tag the part of speech')
		# paddle mode - with a pretrained model
		jieba.enable_paddle()
		# modify the frequency of some useful words
		jieba.suggest_freq(('个','片'), True)
		# more word and be added here...

		# word cutting method 1 (normal mode)
		normal_words = jieba.posseg.cut(text,HMM=False)
		for word, flag in normal_words:
			normal_list.append([word, flag])
		# apppend a terminator with part of speech 'x'
		normal_list.append(['。', 'x'])

		# word cutting method 2 (paddle mode)
		paddle_words = jieba.posseg.cut(text,use_paddle=True)
		for word, flag in paddle_words:
			paddle_list.append([word, flag])

		# get triggerwords through both methods
		normal_keyword_list = self.get_triggerwords_from_normal(normal_list)
		print(normal_keyword_list)
		print("-------------------")
		paddle_keyword_list = self.get_triggerwords_from_paddle(paddle_list)
		print(paddle_keyword_list)
		# compare two results and fill in the forms
		self.fill_in(normal_keyword_list, paddle_keyword_list)

	# trigger words table
		# name: 姓名, 名字
		# age: 年龄, 年纪
		# id: 编号, id, 号码
		# date: 日期, 时间
		# symp: 症状
		# diag: 诊断, 疾病
		# treat: 建议, 方法, 治疗, 意见

	# ########TBD: use dic to store trigger words table
	# get triggerwords using normal methods
	def get_triggerwords_from_normal(self,normal_list):
		from_normal = []
		for i in range(len(normal_list)):
			if normal_list[i][0] == '姓名' or normal_list[i][0] == '名字':
				leng = 2
				input_name = ''
				while normal_list[i+leng][1] != 'x':
					input_name = input_name + normal_list[i+leng][0]
					leng += 1 
				# print(input_name)
				from_normal.append(['name',input_name])
			if normal_list[i][0] == '年龄':
				leng = 1
				input_age = ''
				while normal_list[i+leng][1] != 'x':
					input_age = input_age + normal_list[i+leng][0]
					leng += 1 
				from_normal.append(['age',input_age])
			if normal_list[i][0] == '编号' or normal_list[i][0].lower() == 'id' or normal_list[i][0] == '号码':
				leng = 1
				input_id = ''
				while normal_list[i+leng][1] != 'x':
					input_id = input_id + normal_list[i+leng][0]
					leng += 1 
				from_normal.append(['id',input_id])
			if normal_list[i][0] == '日期' or normal_list[i][0] == '时间':
				leng = 1
				input_date = ''
				while normal_list[i+leng][1] != 'x':
					input_date = input_date + normal_list[i+leng][0]
					leng += 1 
				from_normal.append(['date',input_date])
			if normal_list[i][0] == '症状':
				leng = 3
				input_symp = ''
				while normal_list[i+leng][1] != 'x':
					input_symp = input_symp + normal_list[i+leng][0]
					leng += 1 
				from_normal.append(['symp',input_symp])
			if normal_list[i][0] == '诊断' or normal_list[i][0] == '疾病':
				leng = 1
				input_diag = ''
				while normal_list[i+leng][1] != 'x':
					if normal_list[i+leng][1] != 'p':
						input_diag = input_diag + normal_list[i+leng][0]
					leng += 1 
				from_normal.append(['diag',input_diag])
			if normal_list[i][0] == '建议' or normal_list[i][0] == '方法' or normal_list[i][0] == '治疗' or normal_list[i][0] == '意见':
				leng = 1
				input_treat = ''
				while normal_list[i+leng][1] != 'x':
					if normal_list[i+leng][1] == '：':
						input_treat = ''
					input_treat = input_treat + normal_list[i+leng][0]
					leng += 1 
				from_normal.append(['treat',input_treat])
		return from_normal

	# get triggerwords using paddle methods
	def get_triggerwords_from_paddle(self,paddle_list):
		from_paddle = []
		for i in range(len(paddle_list)):
			if paddle_list[i][0] == '姓名' or paddle_list[i][0] == '名字':
				leng = 2
				input_name = ''
				while leng <= 4:
					if paddle_list[i+leng][1] == 'v':
						break
					if paddle_list[i+leng][1] == 'PER':
						input_name = input_name + paddle_list[i+leng][0]
					leng += 1 
				from_paddle.append(['name',input_name])
			if paddle_list[i][0] == '年龄':
				leng = 1
				input_age = ''
				while leng <= 3:
					if paddle_list[i+leng][1] == 'm':
						input_age = input_age + paddle_list[i+leng][0]
					if paddle_list[i+leng][1] == 'v':
						break
					leng += 1 
				from_paddle.append(['age',input_age])
			if paddle_list[i][0] == '编号' or paddle_list[i][0].lower() == 'id' or paddle_list[i][0] == '号码':
				leng = 1
				input_id = ''
				is_first = 1
				while leng <= 3:
					if paddle_list[i+leng][1] == 'v' and is_first == 1:
						input_id = input_id + paddle_list[i+leng][0]
						is_first = 0
					if paddle_list[i+leng][1] != 'v' and is_first == 0:
						break
					leng += 1 
				from_paddle.append(['id',input_id])
			if paddle_list[i][0] == '日期' or paddle_list[i][0] == '时间':
				leng = 1
				input_date = ''
				while leng <= 3:
					if paddle_list[i+leng][1] == 'TIME':
						input_date = input_date + paddle_list[i+leng][0]
					leng += 1 
				from_paddle.append(['date',input_date])
			if paddle_list[i][0] == '症状':
				leng = 1
				input_symp = ''
				is_sym = 0
				while leng <= 20:
					if paddle_list[i+leng][0] == '。':
						break
					if is_sym == 1:
						input_symp = input_symp + paddle_list[i+leng][0]
					if paddle_list[i+leng][0] == '：':
						is_sym = 1
					if paddle_list[i+leng][1] == 'nz':
						break
					leng += 1 
				from_paddle.append(['symp',input_symp])
			if paddle_list[i][0] == '诊断' or paddle_list[i][0] == '疾病':
				leng = 1
				input_diag = ''
				while leng <= 20:
					input_diag = input_diag + paddle_list[i+leng][0]
					if paddle_list[i+leng][1] == 'nz':
						break
					leng += 1 
				from_paddle.append(['diag',input_diag])
			if paddle_list[i][0] == '建议' or paddle_list[i][0] == '方法' or paddle_list[i][0] == '治疗' or paddle_list[i][0] == '意见':
				leng = 1
				input_treat = ''
				while i+leng < len(paddle_list):
					input_treat = input_treat + paddle_list[i+leng][0]
					leng += 1 
				from_paddle.append(['treat',input_treat])
		return from_paddle

	# fill in the EHR form
	def fill_in(self,normal_keyword_list,paddle_keyword_list):
		for i in range(len(normal_keyword_list)):
			if normal_keyword_list[i][0] == 'name':
				fill_name = self.select(normal_keyword_list[i][1],paddle_keyword_list[i][1])
				self.EHR_View.plainTextEdit_Name.setPlainText(fill_name)
			if normal_keyword_list[i][0] == 'id':
				fill_id = self.select(normal_keyword_list[i][1],paddle_keyword_list[i][1])
				self.EHR_View.plainTextEdit_ID.setPlainText(fill_id)
			if normal_keyword_list[i][0] == 'date':
				fill_date = self.select(normal_keyword_list[i][1],paddle_keyword_list[i][1])
				self.EHR_View.plainTextEdit_Date.setPlainText(fill_date)
			if normal_keyword_list[i][0] == 'symp':
				fill_symp = self.select(normal_keyword_list[i][1],paddle_keyword_list[i][1])
				self.EHR_View.plainTextEdit_Sympotom.setPlainText(fill_symp)
			if normal_keyword_list[i][0] == 'diag':
				fill_diag = self.select(normal_keyword_list[i][1],paddle_keyword_list[i][1])
				self.EHR_View.plainTextEdit_Disease.setPlainText(fill_diag)
			if normal_keyword_list[i][0] == 'treat':
				fill_treat = self.select(normal_keyword_list[i][1],paddle_keyword_list[i][1])
				self.EHR_View.plainTextEdit_Treatment.setPlainText(fill_treat)
		
	# compare two tokens
	def select(self,normal,paddle):
		# if two tokens are the same, keep it
		if normal == paddle:
			return normal
		# if not the same, select the same part
		else:
			res = ''
			for x in normal:
				if x in paddle:
					res = res + x
			return res

