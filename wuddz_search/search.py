"""
░██╗░░░░░░░██╗██╗░░░██╗██████╗░██████╗░███████╗░░░░░░░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗░
░██║░░██╗░░██║██║░░░██║██╔══██╗██╔══██╗╚════██║░░░░░░██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║░
░╚██╗████╗██╔╝██║░░░██║██║░░██║██║░░██║░░███╔═╝█████╗╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║░
░░████╔═████║░██║░░░██║██║░░██║██║░░██║██╔══╝░░╚════╝░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║░
░░╚██╔╝░╚██╔╝░╚██████╔╝██████╔╝██████╔╝███████╗░░░░░░██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║░
░░░╚═╝░░░╚═╝░░░╚═════╝░╚═════╝░╚═════╝░╚══════╝░░░░░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░

 [*]Descr:     ALL IN 1, FILE SEARCH/COPY/MOVE/DEL, REGEX PATTERN PARSER, FILE/FOLDER ARCHIVER        
 [*]Coder:     Wuddz_Devs                                                                             
 [*]Email:     wuddz_devs@protonmail.com                                                              
 [*]Github:    https://github.com/wuddz-devs                                                          
 [*]Telegram:  https://t.me/wuddz_devs                                                                
 [*]Youtube:   wuddz-devs                                                                             

 [*]Search Folder:                                                                                    
    Folder ->  e.g c:\\users\\user\\documents | /home/kali/Documents                                     
    e      ->  Exit Program                                                                           
           ->  Hit Return|Enter Key To Search OS Platform Root Folder                                 
"""

import subprocess, secrets, string, sys, re, time, shutil, signal, getpass
from os import kill, name, system, path, sep, getpid
from pathlib import Path
system('')


class Wuddz_Search():
    def __init__(self):
        self.pkg=str(Path.home().expanduser().joinpath('Downloads','SEARCH'))
        self.lf=Path(self.pkg).joinpath('file.lst')
        self.da=Path(self.pkg).joinpath('archive.7z')
        self.pf=Path(self.pkg).joinpath('archive-pwd.txt')
        Path(Path(str(self.pkg))).mkdir(parents=True, exist_ok=True)
    
    def clear_screen(self):
        if name=='nt':system('cls')
        else:system('clear')
    
    def get_menu(self):
        a=input('\n\033[1;32;40m...Hit Enter|Return Key To Continue....\033[0m\n') or None
        if a:return
    
    def file_size(self,val):
        if val<1024:val=f'{val}B'
        elif val>1024 and val<1048576:val=f'{val/1024:.1f}KB'
        elif val>1048576 and val<1073741824:val=f'{val/1048576:.2f}MB'
        elif val>1073741824:val=f'{val/1073741824:.2f}GB'
        return val
    
    def out_dir(self,epath):
        fld=''
        try:
            if Path(epath.parent).is_dir():fld='valid'
        except:pass
        if not fld:epath=Path(self.pkg).joinpath(epath)
        return epath
    
    def enum_list(self,list):
        eout=[]
        total=0
        for i,f in enumerate(list,start=1):
            me=''
            try:
                mt=time.ctime(Path.stat(f).st_mtime)
                total+=Path.stat(f).st_size
                fs=self.file_size(Path.stat(f).st_size)
                eout.append(f'{i} {f}'+' '*4+str(fs)+' '*4+mt)
                me='boss'
            except:pass
            if not me:eout.append(f'{i} {f}')
        total=self.file_size(total)
        eout.append('Total File Size►► '+str(total))
        return eout

    def enum_output(self,list,fpath,elst):
        """
 [*]Save, Archive, Copy, Move, Delete Files In List:                                            
    1            ->  Archive Files In List To Password Protected Archive [Extensions: zip or 7z]
    2            ->  Copy File/Folder                                                           
    3            ->  Move File/Folder                                                           
    4            ->  Delete File/Folder                                                         
    5            ->  Parse Files In List For Regex Pattern                                      
    file.txt     ->  Save File List As Text In file.txt File [e.g output.txt]                   
    archive.ext  ->  Archive Files In List To archive.ext [Extensions: zip, 7z, tar]            
    b            ->  Back To Previous Screen                                                    
    e            ->  Exit Program                                                               
"""
        extensions=['zip', '7z', 'tar']
        while True:
            try:
                self.clear_screen()
                for e in elst[:-1]:print(e)
                print('\033[1;34;40m'+elst[-1]+'\033[0m')
                epath=input("\033[1;32;40m"+self.enum_output.__doc__+"\033[0m\nInput Choice=> ") or '0'
                if epath!='0':
                    if any(e in epath for e in extensions) or epath=='1':
                        lst=str(self.lf)
                        if epath=='1':
                            epath=self.out_dir(input("Input Archivename=> ") or str(self.da))
                            pkk=getpass.getpass("Input Password Or Get Random Password=> ") or '0'
                            if pkk=='0':pkk=''.join(secrets.choice(string.printable.strip()) for i in range(32))
                            sub="subprocess.call(['7z', 'a', '-t'+str(epath).split('.')[1], epath, '@'+lst, '-mx9', '-p'+pkk])"
                            pwf=str(Path(epath).stem).split('.')[0]
                            with open(str(self.pf).replace('archive',pwf), 'w') as ps:
                                ps.write("'"+str(Path(epath).resolve())+"'\n"+str(pkk)+'\n'+'_'*146+'\n\n')
                        else:
                            epath=self.out_dir(epath)
                            sub="subprocess.call(['7z', 'a', '-t'+str(epath).split('.')[1], epath, '@'+lst, '-mx9'])"
                        with open(lst, 'w') as bn:
                            [bn.write(f'{file}\n') for file in list]
                        eval(sub)
                        print("\n\033[1;34;40m['"+str(Path(epath).resolve())+"']► Files Archived Successfully\033[0m")
                        Path(lst).unlink()
                    elif epath=='2' or epath=='3':
                        src=input("Input Source File/Folder Path=> ") or '0'
                        des=input("Input Destination File/Folder Path=> ") or '0'
                        if Path(src).exists() and Path(des).exists():
                            if epath=='2':
                                if Path(src).is_file():shutil.copy(src,des)
                                else:
                                    des=f'{des}\\'+src.split('\\')[-1]
                                    shutil.copytree(src,des,dirs_exist_ok=True,symlinks=True)
                            else:shutil.move(src,des)
                    elif epath=='4':
                        fl=input("Input File/Folder Path To Delete=> ") or '0'
                        if Path(fl).is_file():Path(fl).unlink()
                        else:shutil.rmtree(fl)
                    elif epath=='5':self.regex_search(list)
                    elif '.txt' in epath:
                        epath=self.out_dir(epath)
                        with open(epath, 'w', encoding='utf-8') as ep:
                            [ep.write(f'{e}\n') for e in elst]
                    elif epath=='b':break
                    elif epath=='e':kill(getpid(),signal.SIGTERM)
                    self.get_menu()
            except:pass

    def regex_search(self,list):
        """
 [*]Parse Files In List For Regex Pattern:   
    1  ->  IPTVURL                           
    2  ->  IP+IP:PORT                        
    3  ->  URL                               
    4  ->  MAC                               
    5  ->  EMAIL:PASS                        
    6  ->  USER:PASS                         
    r  ->  Regex Pattern  [e.g \w+server:\w+]
    b  ->  Back To Previous Screen           
    e  ->  Exit Program                      
"""
        while True:
            self.clear_screen()
            plst=[]
            rp=input("\033[1;32;40m"+self.regex_search.__doc__+"\033[0m\nInput Choice=> ") or '0'
            if rp=='b':break
            elif rp=='e':kill(getpid(),signal.SIGTERM)
            else:
                for file_name in list:
                    if Path(file_name).is_file():
                        with open(file_name, 'r', encoding="utf8", errors ='replace') as f:
                            if rp=='1':
                                [plst.append(a) for b in (x for x in f) for a in re.compile('h\w+://[\w\-\.]+:?\w+/?').findall(b)]
                            elif rp=='2':
                                [plst.append(a) for b in (x for x in f) for a in re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:?\d{1,5}').findall(b)]
                            elif rp=='3':
                                [plst.append(a) for b in (x for x in f) for a in re.compile('\w+://[\w\-\.]+.*$').findall(b)]
                            elif rp=='4':
                                [plst.append(a) for b in (x for x in f) for a in re.compile('\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}').findall(b)]
                            elif rp=='5':
                                [plst.append(a) for b in (x for x in f) for a in re.compile('[\w\.-]+@[\w\.-]+:[\w\.-]+').findall(b)]
                            elif rp=='6':
                                [plst.append(a) for b in (x for x in f) for a in re.compile('^[\w\.-]+:[\w\.-]+$').findall(b)]
                            elif rp[0]=='r':
                                rpat=input('Input Regex Pattern=> ') or '0'
                                if rpat!='0':
                                    [plst.append(a) for b in (x for x in f) for a in re.compile(rp.split('r')[1]).findall(b)]
                if plst:self.regex_output(plst)

    def regex_output(self,lst):
        """
 [*]Save Parsed Regex Output To File:                                                 
    File.ext  ->  File To Save Parsed Regex Output  [e.g regex.txt]                   
              ->  Hit Return|Enter Key To Save To Default File  [i.e regex_output.txt]
"""
        self.clear_screen()
        rego=input("\033[1;32;40m"+self.regex_output.__doc__+"\033[0m\nInput File=> ") or 'regex_output.txt'
        rlst=sorted(set(lst))
        with open(rego, 'w', encoding='utf-8') as out:
            [out.write(f'{r}\n') for r in rlst]
    
    def search_type(self,fpath):
        """
 [*]Search Types [.ext = File Extension Of Choice]:                                                                 
    link.txt ->  Find "link.txt" File                                                                               
    *.ext    ->  Find All Files With .ext File Extension [e.g *.txt Find All Text Files]                            
    test*    ->  Find All Files With Filename Starting With "test" [.ext Optional e.g test*.jpg Files]              
    *test    ->  Find All Files With Filename Ending With "test" [.ext Optional e.g *test.txt Files]                
    *test*   ->  Find All Files With "test" Anywhere In Filename [.ext Optional e.g *test*.py Files]                
    *te*st*  ->  Find All Files With "te" Followed By "st" Anywhere In Filename [.ext Optional e.g *te*st*.py Files]
    c        ->  Change Search Folder                                                                               
    e        ->  Exit Program                                                                                       
             ->  Hit Return To Find All Files In Folder                                                             
"""
        flst=[]
        while True:
            try:
                self.clear_screen()
                stype=input("\033[1;32;40m"+self.search_type.__doc__+"\033[0m\nInput Search Type=> ") or '*'
                if stype=='c':break
                elif stype=='e':kill(getpid(),signal.SIGTERM)
                else:
                    flst=list(Path(fpath).rglob(stype))
                    if flst:
                        elst=self.enum_list(flst)
                        self.enum_output(flst,fpath,elst)
            except:pass
    
    def main(self):
        while True:
            try:
                self.clear_screen()
                fpath=input("\033[1;32;40m"+__doc__+"\033[0m\nInput Folder=> ") or path.abspath(sep)
                if Path(fpath).is_dir():
                    self.search_type(fpath)
                elif fpath=='e':kill(getpid(),signal.SIGTERM)
            except:pass

Wuddz_Search().main()