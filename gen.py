#!/usr/bin/python3

import os
import os.path



def dealfile(dpath):
	print('dealing with', dpath)
	a = open(os.path.join(dpath, 'index.html'), 'wb')
	for f in os.listdir(dpath):
		if os.path.isdir(os.path.join(dpath, f)):
			nDir = os.path.join(dpath, f)
			print(nDir)
			nFile = os.path.join(nDir, 'index.html')
			#print(nFile)
			if not os.path.exists(nFile):
			# 文件夹创建一个index.html
				b =open(nFile, 'ab')
				b.write(' '.encode('utf-8'))
				b.close()
			dealfile(nDir)
		if f.find('mp4') >= 0 or os.path.isdir(os.path.join(dpath, f)):
			nDir = os.path.join(dpath, f)
			nDir = nDir.replace('/home/leon/coursera', 'http://zhangyf.xyz')
			a.write('<p><a href=\''.encode('utf-8'))
			a.write(nDir.encode('utf-8'))
			a.write('\'>'.encode('utf-8'))
			a.write(f.encode('utf-8'))
			a.write('</a></p>\n'.encode('utf-8'))
			
			
	a.close()
dealfile(os.getcwd())
