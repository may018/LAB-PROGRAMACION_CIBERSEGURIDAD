#! /usr/bin/python # -*- coding: utf-8 -*
import os
import re
import sys
import datetime,time 
import ftplib 
import FTP
import traceback
import logging
 
 LOG_FORMAT = "% (message) s" # "% (asctime) s% (name) s% (levelname) s% (pathname) s% (message) s" 
 DATE_FORMAT = '% Y-% m-% d% H:% M:% S% a'
LOG_PATH = None#os.path.join(os.getcwd(),'./logs/ftpget.log')
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt = DATE_FORMAT ,
                                         filemode = 'a', 
                                         filename = LOG_PATH 
                    )
 

def IsDownloadCompletely(RemoteFile, LocalFile, remote_size):
    p = re.compile(r'\\',re.S)
    LocalFile = p.sub('/', LocalFile)
    localsize = os.path.getsize(LocalFile)
    if localsize == remote_size:
        print('downloading  %s ...Successs! remote_size:%d , local_size:%d.' %(RemoteFile, remote_size, localsize))
        logging.debug('downloading  %s ... Successs! remote_size:%d , local_size:%d.' %(RemoteFile, remote_size, localsize))
        return True
    else:
        print('downloading  %s ...Successs! remote_size:%d , local_size:%d.' %(RemoteFile, remote_size, localsize))
        logging.debug('downloading  %s ... Successs! remote_size:%d , local_size:%d.' %(RemoteFile, remote_size, localsize))
        return False
 

def ftp_download(LocalFile, RemoteFile, bufsize, ftp):

    if not os.path.exists(LocalFile):
        with open(LocalFile, 'wb') as f:
            ftp.retrbinary('RETR %s' % RemoteFile, f.write, bufsize)

        return IsDownloadCompletely(RemoteFile, LocalFile, bufsize)
    else:
        if not IsDownloadCompletely(RemoteFile, LocalFile, bufsize):
            with open(LocalFile, 'wb+') as f:
                ftp.retrbinary('RETR %s' % RemoteFile, f.write, bufsize)

            return IsDownloadCompletely(RemoteFile, LocalFile, bufsize)

def DownLoadRUledFile(LocalDir, RemoteDir, filename, ftp):
    print("RemoteDir:", RemoteDir)
 
    if not os.path.exists(LocalDir):
        os.makedirs(LocalDir)
         Local = os.path.join (LocalDir, nombre de archivo) 
    try:

        ftp.cwd(RemoteDir)
               
                 ftp.voidcmd ('TYPE I') 
                 bufsize = ftp.size (nombre de archivo)
        ftp_download(Local, filename, bufsize, ftp)
    except:
        print('some error happend in get file:%s. Err:%s' %(filename, traceback.format_exc()))
        logging.debug('some error happend in get file:%s. Err:%s' %(filename, traceback.format_exc()))
    
    return
 

def DownLoadFileTree(LocalDir, RemoteDir, ftp, IsRecursively=False):
    print("RemoteDir:", RemoteDir)
 
    if not os.path.exists(LocalDir):
        print('local directory %s not exists , make it ...')
        os.makedirs(LocalDir)

    ftp.cwd(RemoteDir)
    dir_list = []
         '' 'Dirige el directorio actual y coloca el resultado en la lista' ''
    ftp.dir('.', dir_list.append)
    for dif in dir_list:
        if dif.startswith("d"):
            if IsRecursively:
                                 '' 'El objeto es un directorio Descarga recursiva' ''
                print('%s is a directory, download it Recursively...' %(dif))
                p_subdir = dif.split(" ")[-1]
                p_local_subdir = os.path.join(LocalDir, p_subdir)
                                 '' 'El principio de crear subdirectorios locales
                p_remote_subdir = os.path.join(ftp.pwd(), p_subdir)
                DownLoadFileTree(p_local_subdir, p_remote_subdir, ftp)
                                 ftp.cwd ("..") #
            else:
                print('%s es directorio, se esta descargando recursivamente...' %(dif))
                continue
        else:
                         '' 'Es un archivo para descargar directamente' ''
            print('%s es un archivo, descargando... %(dif))
            p_filename = dif.split(" ")[-1]
                         bufsize = ftp.size (p_filename) 
                         Localfile = os.path.join (LocalDir, p_filename)
            ftp_download(Localfile, p_filename, bufsize, ftp)
    return
if __name__ == '__main__':  
    host = 'Direccion IP del servidor FTP'
    port = 21
    username = 'Usuario del servidor'
    password = 'Contraseña del servidor'
    ftp = FTP()
    ftp.connect(host,port)
    ftp.login(username, password)

    LocalDir = os.getcwd()
    RemoteDir = '/home/li'
    filename = 'readme.txt'

         '' 'Descargar todo el directorio de forma recursiva' ''
         IsRecursively = True 
    DownLoadFileTree(LocalDir, RemoteDir, ftp, IsRecursively)