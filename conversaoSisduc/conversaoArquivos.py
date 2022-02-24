# -*- coding: utf-8 -*-
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
########################################################################################################################################################################
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##-- Finalidade: Conversao de arquivos
##-- Tecnicos: Bruno Rodrigues de Oliveira
##-- Creditos: DIGEO
##-- Descricao: Conversao de arquivos
##--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
########################################################################################################################################################################

import sys, os
import shutil
import PyPDF2
from PIL import Image
Image.MAX_IMAGE_PIXELS = None


class pastaConversao():
	def __init__(self, caminhoPasta):
		self.listaArquivos = os.listdir(caminhoPasta)
		self.listaProjetos = []
		self.listaProjetosNovos = []
		self.listaImagens = []
		self.basename = os.path.basename(caminhoPasta)
		self.newPath = os.path.join(caminhoPasta,self.basename+"_edit")
		self.number = ''
		self.ano = ''
		self.caminhoPasta = caminhoPasta

	def checkNumber(self, value):
		if value < 10:
			self.number = '00'+str(value)
		elif (value >= 10) and (value < 100):
			self.number = '0'+str(value)
		else:
			self.number = str(value)

	def checkAno(self, value):
		if value < 10:
			self.ano = '200'+str(value)
		elif (value >= 10) and (value < 30):
			self.ano = '20'+str(value)
		elif (value >= 30):
			self.ano = '19'+str(value)
		else:
			self.ano = 'CONFERIR'

	def recuperarProjetosALT (self):
		for arquivo in self.listaArquivos:
			if (arquivo.endswith(".jpeg")) or (arquivo.endswith(".jpg") or (arquivo.endswith(".tif") or (arquivo.endswith(".png")))):
				arquivoNome = (arquivo.upper()).split(" FL")[0]
				if arquivoNome not in self.listaProjetos:
					arquivoTemp1 = (((arquivoNome.replace(' ','_')).replace('-','_')).upper())
					arquivoNumero = int(arquivoTemp1[4:6].replace('_',''))
					arquivoAno = int(arquivoTemp1[-2:])
					self.checkNumber(arquivoNumero)
					self.checkAno(arquivoAno)
					arquivoNovo = "%s_%s_%s" % (self.basename, self.number, self.ano)
					self.listaProjetos.append(arquivoNome)
					self.listaProjetosNovos.append(arquivoNovo)

	def recuperarProjetosSEMPR (self, setor):
		for arquivoNome in self.listaArquivos:
			if (arquivoNome.endswith(".jpeg")) or (arquivoNome.endswith(".jpg") or (arquivoNome.endswith(".tif") or (arquivoNome.endswith(".png")))):
				if arquivoNome not in self.listaProjetos:
					if 'SEM PR' not in arquivoNome:
						#arquivoNovo = 'SEM_PR_' + arquivoNome
						arquivoNovo =  arquivoNome
						arquivoNovo = ((((setor +'_'+ (((arquivoNovo.replace(' ','_')).replace('-','_')).upper())).replace('.JPG','')).replace('.PNG','')).replace('.TIF','')).replace('.JPEG','')
					else:
						arquivoNovo = ((((setor +'_'+ (((arquivoNome.replace(' ','_')).replace('-','_')).upper())).replace('.JPG','')).replace('.PNG','')).replace('.TIF','')).replace('.JPEG','')
					self.listaProjetos.append(arquivoNome)
					self.listaProjetosNovos.append(arquivoNovo)
		print(self.listaProjetosNovos)

	def recuperarProjetosPT (self, setor):
		for arquivoNome in self.listaArquivos:
			if (arquivoNome.endswith(".jpeg")) or (arquivoNome.endswith(".jpg") or (arquivoNome.endswith(".tif") or (arquivoNome.endswith(".png")))):
				if arquivoNome not in self.listaProjetos:
					arquivoNovo = ((((setor +'_'+ (((arquivoNome.replace(' ','_')).replace('-','_')).upper())).replace('.JPG','')).replace('.PNG','')).replace('.TIF','')).replace('.JPEG','')
					self.listaProjetos.append(arquivoNome)
					self.listaProjetosNovos.append(arquivoNovo)
		print(self.listaProjetosNovos)

	def recuperarProjetosPR (self, setor):
		for arquivoNome in self.listaArquivos:
			if (arquivoNome.endswith(".jpeg")) or (arquivoNome.endswith(".jpg") or (arquivoNome.endswith(".tif") or (arquivoNome.endswith(".png")))):
				if arquivoNome not in self.listaProjetos:
					arquivoNovo = ((((setor +'_'+ (((arquivoNome.replace(' ','_')).replace('-','_')).upper())).replace('.JPG','')).replace('.PNG','')).replace('.TIF','')).replace('.JPEG','')
					self.listaProjetos.append(arquivoNome)
					self.listaProjetosNovos.append(arquivoNovo)
		print(self.listaProjetosNovos)

	def recuperarProjetosCI (self, setor):
		for arquivoNome in self.listaArquivos:
			if ((arquivoNome.endswith(".jpeg")) or (arquivoNome.endswith(".jpg")) or (arquivoNome.endswith(".TIF")) or (arquivoNome.endswith(".tif")) or (arquivoNome.endswith(".png"))):
				print(arquivoNome)
				if arquivoNome not in self.listaProjetos:
					arquivoNovo = (setor +'_'+ ((((((arquivoNome.replace(' ','_')).replace('-','_')).upper())).replace('.JPG','')).replace('.PNG','')).replace('.TIF','')).replace('.JPEG','')
					self.listaProjetos.append(arquivoNome)
					self.listaProjetosNovos.append(arquivoNovo)
		print(self.listaProjetosNovos)

	def recuperarProjetosPLN (self):
		print(self.listaArquivos)
		for arquivo in self.listaArquivos:
			if (arquivo.endswith(".jpeg")) or (arquivo.endswith(".jpg") or (arquivo.endswith(".tif") or (arquivo.endswith(".png")))):
				arquivoNome = (arquivo.upper()).split(" FL")[0]
				if arquivoNome not in self.listaProjetos:
					arquivoTemp1 = (arquivoNome.upper()).replace('.JPG','')
					arquivoNumero = int((arquivoTemp1.split(" ")[1]).split("_")[0])
					arquivoAno = int(arquivoTemp1[-2:])
					self.checkNumber(arquivoNumero)
					self.checkAno(arquivoAno)
					arquivoNovo = "%s_%s_%s" % (self.basename, self.number, self.ano)
					self.listaProjetos.append(arquivoNome)
					self.listaProjetosNovos.append(arquivoNovo)

	def recuperarProjetosURB (self):
		print('ARQUIVOS', self.listaArquivos)
		for arquivo in self.listaArquivos:
			if (arquivo.endswith(".jpeg")) or (arquivo.endswith(".jpg") or (arquivo.endswith(".tif") or (arquivo.endswith(".png")))):
				arquivoNome = (arquivo.upper()).split(" FL")[0]
				if arquivoNome not in self.listaProjetos:
					arquivoTemp1 = ((arquivoNome.upper()).replace('.JPG','')).replace('-','_')
					if arquivoTemp1 != 'THUMBS.DB':
						arquivoNumero = int((arquivoTemp1.split(" ")[1]).split("_")[0])
						arquivoAno = int(arquivoTemp1[-2:])
						print('NUMERO:',arquivoNumero, 'ANO:',arquivoAno)
						self.checkNumber(arquivoNumero)
						self.checkAno(arquivoAno)
						arquivoNovo = "%s_%s_%s" % (self.basename, self.number, self.ano)
						self.listaProjetos.append(arquivoNome)
						self.listaProjetosNovos.append(arquivoNovo)

	def recuperarProjetosPSG (self):
		print('ARQUIVOS', self.listaArquivos)
		for arquivo in self.listaArquivos:
			if (arquivo.endswith(".jpeg")) or (arquivo.endswith(".jpg") or (arquivo.endswith(".tif") or (arquivo.endswith(".png")))):
				arquivoNome = (arquivo.upper()).split(" FL")[0]
				if arquivoNome not in self.listaProjetos:
					arquivoTemp1 = (((arquivoNome).replace('-','_')).upper())
					arquivoNumero = int((arquivoTemp1.split(" ")[1]).split("_")[0])
					arquivoAno = int(arquivoTemp1[-2:])
					print('NUMERO:',arquivoNumero, 'ANO:',arquivoAno)
					self.checkNumber(arquivoNumero)
					self.checkAno(arquivoAno)
					arquivoNovo = "%s_%s_%s" % (self.basename, self.number, self.ano)
					self.listaProjetos.append(arquivoNome)
					self.listaProjetosNovos.append(arquivoNovo)
	
	def recuperarProjetosMDE (self, caminhoPasta): #MDE 97_87.pdf
		if os.path.exists(self.newPath):
			print('Caminho ja existe.')
		else:
			os.mkdir(self.newPath)
		for arquivo in self.listaArquivos:
			arquivoOrigem = os.path.join(caminhoPasta, arquivo)
			#arquivoTemp1 = (((arquivo.replace(' ','_')).replace('-','_')).upper()).replace('.PDF','')
			arquivoTemp1 = ((arquivo.upper()).replace('.PDF','')).replace('-','_')
			if (arquivoTemp1 != 'THUMBS.DB'):
				arquivoNumero = int((arquivoTemp1.split(" ")[1]).split("_")[0])
				#arquivoNumero = int(arquivoTemp1[4:6])
				arquivoAno = int(arquivoTemp1[-2:])
				print('NUMERO:',arquivoNumero, 'ANO:',arquivoAno)
				self.checkNumber(arquivoNumero)
				self.checkAno(arquivoAno)
				arquivoNovo = "%s_%s_%s" % (self.basename.replace('-','_'), self.number, self.ano)
				arquivoDestino = os.path.join(self.newPath, arquivoNovo)+'.pdf'
				os.rename(arquivoOrigem, arquivoDestino)

	def recuperarProjetosNGB (self, caminhoPasta): #MDE 97_87.pdf
		if os.path.exists(self.newPath):
			print('Caminho ja existe.')
		else:
			os.mkdir(self.newPath)
		for arquivo in self.listaArquivos:
			arquivoOrigem = os.path.join(caminhoPasta, arquivo)
			arquivoTemp1 = ((arquivo.upper()).replace('.PDF','')).replace('-','_')
			if arquivoTemp1 != 'THUMBS.DB':
				arquivoNumero = int((arquivoTemp1.split(" ")[1]).split("_")[0])
				#arquivoNumero = int(arquivoTemp1[4:6])
				arquivoAno = int(arquivoTemp1[-2:])
				print('NUMERO:',arquivoNumero, 'ANO:',arquivoAno)
				self.checkNumber(arquivoNumero)
				self.checkAno(arquivoAno)
				arquivoNovo = "%s_%s_%s" % (self.basename.replace('-','_'), self.number, self.ano)
				arquivoDestino = os.path.join(self.newPath, arquivoNovo)+'.pdf'
				os.rename(arquivoOrigem, arquivoDestino)

	def recuperarProjetosTOP (self):
		print('ARQUIVOS', self.listaArquivos)
		for arquivo in self.listaArquivos:
			if (arquivo.endswith(".jpeg")) or (arquivo.endswith(".jpg") or (arquivo.endswith(".tif") or (arquivo.endswith(".png")))):
				arquivoNome = (arquivo.upper()).split(" FL")[0]
				if arquivoNome not in self.listaProjetos:
					arquivoTemp1 = (((arquivoNome.replace(' ','_')).replace('-','_')).upper())
					arquivoNumero = int((arquivoTemp1[4:7].replace('_','')).replace(' ',''))
					arquivoAno = int(arquivoTemp1[-2:])
					print('NUMERO:',arquivoNumero, 'ANO:',arquivoAno)
					self.checkNumber(arquivoNumero)
					self.checkAno(arquivoAno)
					arquivoNovo = "%s_%s_%s" % (self.basename, self.number, self.ano)
					self.listaProjetos.append(arquivoNome)
					self.listaProjetosNovos.append(arquivoNovo)

	def recuperarProjetosDET (self):
		print('ARQUIVOS', self.listaArquivos)
		for arquivo in self.listaArquivos:
			if (arquivo.endswith(".jpeg")) or (arquivo.endswith(".jpg") or (arquivo.endswith(".tif") or (arquivo.endswith(".png")))):
				arquivoNome = (arquivo.upper()).split(" FL")[0]
				if arquivoNome not in self.listaProjetos:
					#arquivoTemp1 = (((arquivoNome.replace(' ','_')).replace('-','_')).upper())
					#arquivoNumero = int((arquivoTemp1[4:7].replace('_','')).replace(' ',''))
					arquivoTemp1 = (arquivoNome.upper()).replace('.JPG','')
					arquivoNumero = int((arquivoTemp1.split(" ")[1]).split("_")[0])
					arquivoAno = int(arquivoTemp1[-2:])
					print('NUMERO:',arquivoNumero, 'ANO:',arquivoAno)
					self.checkNumber(arquivoNumero)
					self.checkAno(arquivoAno)
					arquivoNovo = "%s_%s_%s" % (self.basename, self.number, self.ano)
					self.listaProjetos.append(arquivoNome)
					self.listaProjetosNovos.append(arquivoNovo)


	def recuperarProjetosPUR (self, caminhoPasta): #MDE 97_87.pdf
		if os.path.exists(self.newPath):
			print('Caminho ja existe.')
		else:
			os.mkdir(self.newPath)
		for arquivo in self.listaArquivos:
			arquivoOrigem = os.path.join(caminhoPasta, arquivo)
			#arquivoTemp1 = (((arquivo.replace(' ','_')).replace('-','_')).upper()).replace('.PDF','')
			arquivoTemp1 = ((arquivo.upper()).replace('.PDF','')).replace('-','_')
			if (arquivoTemp1 != 'THUMBS.DB'):
				arquivoNumero = int((arquivoTemp1.split(" ")[1]).split("_")[0])
				#arquivoNumero = int(arquivoTemp1[4:6])
				arquivoAno = int(arquivoTemp1[-2:])
				print('NUMERO:',arquivoNumero, 'ANO:',arquivoAno)
				self.checkNumber(arquivoNumero)
				self.checkAno(arquivoAno)
				arquivoNovo = "%s_%s_%s" % (self.basename.replace('-','_'), self.number, self.ano)
				arquivoDestino = os.path.join(self.newPath, arquivoNovo)+'.pdf'
				os.rename(arquivoOrigem, arquivoDestino)

	def converterImagens(self):
		if os.path.exists(self.newPath):
			print('Caminho ja existe.')
		else:
			os.mkdir(self.newPath)
		i = 0
		for projeto in self.listaProjetos:
			self.listaImagens = []
			for arquivo in self.listaArquivos:
				if arquivo != 'Thumbs.db':
					if projeto in arquivo:
						self.listaImagens.append(Image.open(os.path.join(caminhoPasta,arquivo)))
			try:
				self.listaImagens.sort()
				imageOne = self.listaImagens[0].convert('RGB')
				outfile = self.listaProjetosNovos[i]+".pdf"
				outPath = os.path.join(self.newPath, outfile)
				imageOne.save(outPath,save_all=True, append_images=self.listaImagens[1:])
				i += 1
			except:
				i += 1
				print(self.listaImagens[0])
				pass
# C:\Python27\ArcGISx6410.7\python.exe I:\COSIT_SITURB\TECNICOS\TRABALHO_ELABORACAO\Bruno_Rodrigues\9_sisduc\conversaoArquivos.py

if __name__ == '__main__':
	setor = 'CSSMA'
	folders = os.listdir(r"I:\\COSIT_SITURB\\TECNICOS\\TRABALHO_ELABORACAO\\Bruno_Rodrigues\\9_sisduc\\CONVERTER")
	for pasta  in folders:
		if pasta != 'Thumbs.db':
			caminhoPasta = os.path.join(r"I:\\COSIT_SITURB\\TECNICOS\\TRABALHO_ELABORACAO\\Bruno_Rodrigues\\9_sisduc\\CONVERTER",pasta)
			pasta = pastaConversao(caminhoPasta)
			if pasta.basename == 'ALT':
				pasta.recuperarProjetosALT()
				pasta.converterImagens()
			elif pasta.basename == 'PNRC': #PROJETOS NAO REGISTRADOS EM CARTORIO
				pass
			elif pasta.basename == 'PT': #SEM INFORMACAO
				pasta.recuperarProjetosPT(setor)
				pasta.converterImagens()
			elif pasta.basename == 'SEM PR': #PROJETOS SEM PR
				pasta.recuperarProjetosSEMPR(setor)
				pasta.converterImagens()
			elif pasta.basename == 'PR': #PROJETOS SEM PR
				pasta.recuperarProjetosPR(setor)
				pasta.converterImagens()
			elif pasta.basename == 'CI': #PROJETOS
				pasta.recuperarProjetosCI(setor)
				pasta.converterImagens()
			elif pasta.basename == 'MDE' or pasta.basename == 'MDE-RP': #MEMORIAL DESCRITIVO
				pasta.recuperarProjetosMDE(caminhoPasta)
				#pasta.converterImagens()
			elif pasta.basename == 'NGB'or pasta.basename == 'NGB-RP': #NORMAS DE GABARITO
				pasta.recuperarProjetosNGB(caminhoPasta)
			elif pasta.basename == 'PLN': #PROJETOS 
				pasta.recuperarProjetosPLN()
				pasta.converterImagens()
			elif pasta.basename == 'URB'or pasta.basename == 'URB-PH' or pasta.basename == 'URB-RP-DET' or pasta.basename == 'URB-RP': #PROJETOS URBANISTICOS
				pasta.recuperarProjetosURB()
				pasta.converterImagens()
			elif pasta.basename == 'PSAA': #PROJETOS SUBSTITUIDOS_ANULADOS_ALTERADOS
				pass
			elif pasta.basename == 'JA': #PROJETOS SUBSTITUIDOS_ANULADOS_ALTERADOS
				pasta.recuperarProjetosPR(setor)
				pasta.converterImagens()
			elif pasta.basename == 'PSG': #PROJETOS DE PAISAGISMO
				pasta.recuperarProjetosPSG()
				pasta.converterImagens()
			elif pasta.basename == 'SIV': #PROJETOS DE SISTEMA VIARIO
				pass
			elif pasta.basename == 'TOP': #SEM INFORMACAO
				pasta.recuperarProjetosTOP()
				pasta.converterImagens()
			elif pasta.basename == 'GERAL':
				pass
			elif pasta.basename == 'PDL': #PLANO DIRETOR LOCAL
				pass
			elif pasta.basename == 'PLANTA GERAL':
				pass
			elif pasta.basename == 'PUR' or pasta.basename == 'PUR-RP': #PARAMETROS URBANISTICOS
				pasta.recuperarProjetosPUR(caminhoPasta)
			elif pasta.basename == 'DET': #DETALHAMENTO
				pasta.recuperarProjetosDET()
				pasta.converterImagens()
			elif pasta.basename == 'DD':
				pasta.recuperarProjetosPR(setor)
				pasta.converterImagens()
			elif pasta.basename == 'POQT': #PLANO DE OCUPACAO DE QUIOSQUES
				pass
			elif pasta.basename == 'DRN':
				pasta.recuperarProjetosDET()
				pasta.converterImagens()
			elif pasta.basename == 'PA':
				pasta.recuperarProjetosPR(setor)
				pasta.converterImagens()
			elif pasta.basename == 'MOB':
				pass
			elif pasta.basename == 'AER':
				pass
			elif pasta.basename == 'PR':
				pass
			elif pasta.basename == 'GB':
				pass