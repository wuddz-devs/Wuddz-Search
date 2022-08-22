"""
░██╗░░░░░░░██╗██╗░░░██╗██████╗░██████╗░███████╗░░░░░░░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗░
░██║░░██╗░░██║██║░░░██║██╔══██╗██╔══██╗╚════██║░░░░░░██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║░
░╚██╗████╗██╔╝██║░░░██║██║░░██║██║░░██║░░███╔═╝█████╗╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║░
░░████╔═████║░██║░░░██║██║░░██║██║░░██║██╔══╝░░╚════╝░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║░
░░╚██╔╝░╚██╔╝░╚██████╔╝██████╔╝██████╔╝███████╗░░░░░░██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║░
░░░╚═╝░░░╚═╝░░░╚═════╝░╚═════╝░╚═════╝░╚══════╝░░░░░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░

 [*]Descr:     ALL IN 1, FILE/FOLDER EXPLORER, REGEX PATTERN PARSER & ARCHIVER (ENCRYPTION OPTIONAL)  
 [*]Coder:     Wuddz_Devs                                                                             
 [*]Email:     wuddz_devs@protonmail.com                                                              
 [*]Github:    https://github.com/wuddz-devs                                                          
 [*]Telegram:  https://t.me/wuddz_devs                                                                
 [*]Videos:    https://mega.nz/folder/IWVAXTqS#FoZAje2NukIcIrEXXKTo0w                                 
 [*]Youtube:   wuddz-devs                                                                             

 [*]Search Folder:                                                                                    
    Folder ->  e.g c:\\users\\user\\documents | /home/kali/Documents                                     
    e      ->  Exit Program                                                                           
           ->  Hit Return|Enter Key To Search OS Root Folder                                          
"""

import secrets, string, sys, re, time, shutil, signal
from os import kill, name, system, path, sep, getpid
from pathlib import Path, PurePath
from getpass import getpass
from subprocess import run, Popen
system('')


class Wuddz_Search:
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
        for i,f in enumerate([x for x in list if Path(x).exists()],start=1):
            me=''
            try:
                mt=time.ctime(Path.stat(f).st_mtime)
                total+=Path.stat(f).st_size
                fs=self.file_size(Path.stat(f).st_size)
                eout.append(f'{i}  {f}'+' '*4+str(fs)+' '*4+mt)
                me='boss'
            except:pass
            if not me:eout.append(f'{i} {f}')
        total=self.file_size(total)
        eout.append('Total File Size►► '+str(total))
        return eout
    
    def list_archive(self,epath,list,sub,dpl=None):
        lst=str(self.lf)
        with open(lst, 'w') as bn:
            [bn.write(f'{file}\n') for file in list]
        if dpl!=None:sub=sub.replace(" epath,", " epath, '-spf',")
        out=eval(sub)
        if 'Everything is Ok' in str(out) and dpl==None:
            print("\n\033[1;34;40m['"+str(Path(epath).resolve())+"']► Files Archived Successfully\033[0m")
        Path(lst).unlink()
    
    def list_modes(self,lst,elst,des=None):
        for e in elst[:-1]:
            fp=e.split('  ')[1]
            for l in lst:
                try:
                    eval(l)
                except:pass
    
    def enum_output(self,list,fpath):
        """
 [*]ARCHIVE, COPY, DELETE, MOVE, OPEN, PARSE, SAVE:                                             
    1            ->  Archive Files In List To Password Protected Archive [Extensions: zip or 7z]
    2            ->  Copy File/Folder Or Entire List                                            
    3            ->  Move File/Folder Or Entire List                                            
    4            ->  Delete File/Folder Or Entire List                                          
    5            ->  Open File                                                                  
    6            ->  Parse Files In List For Regex Pattern                                      
    file.txt     ->  Save File List As Text In file.txt File                                    
    archive.ext  ->  Archive Files In List To archive.ext [Extensions: zip, 7z, tar]            
    b            ->  Back To Previous Screen                                                    
    e            ->  Exit Program                                                               """
        extensions=['zip', '7z', 'tar']
        while True:
            try:
                self.clear_screen()
                elst=self.enum_list(list)
                for e in elst[:-1]:print(e)
                print('\033[1;34;40m'+elst[-1]+'\033[0m')
                epath=input("\033[1;32;40m"+self.enum_output.__doc__+"\033[0m\n\nInput Choice=> ") or '0'
                if epath!='0':
                    if any(e in epath for e in extensions) or epath=='1':
                        ndp=[file for file in list if Path(file).is_file() and not str(list).count(str(PurePath(file).name))>1]
                        dup=[file for file in list if Path(file).is_file() and str(list).count(str(PurePath(file).name))>1]
                        if epath=='1':
                            epath=self.out_dir(input("Input Archive [e.g test.7z]=> ") or str(self.da))
                            self.pkk=getpass("Input Password Or Random Password Used=> ") or '0'
                            if self.pkk=='0':self.pkk=''.join(secrets.choice((string.ascii_letters+string.digits).strip()) for i in range(32))
                            sub="run(['7z', 'a', '-t'+str(epath).split('.')[1], epath, '@'+lst, '-mx9', '-p'+self.pkk], capture_output=True, text=True)"
                            pwf=str(Path(epath).stem).split('.')[0]
                            with open(str(self.pf).replace('archive',pwf), 'w') as ps:
                                ps.write("'"+str(Path(epath).resolve())+"'\n"+str(self.pkk)+'\n'+'_'*146+'\n\n')
                        else:
                            epath=self.out_dir(epath)
                            sub="run(['7z', 'a', '-t'+str(epath).split('.')[1], epath, '@'+lst, '-mx9'], capture_output=True, text=True)"
                        if ndp:self.dups(epath,ndp,sub)
                        if dup:self.dups(epath,dup,sub,dpl='yes')
                    elif epath=='2' or epath=='3':
                        src=input("Input Source File/Folder Or 'a' For Entire List=> ") or '0'
                        des=input("Input Destination Folder Or Default Folder Used=> ") or self.pkg
                        if epath=='2':
                            if src=='a':self.list_modes(['shutil.copy(fp,des)'],elst,des=des)
                            elif Path(src).is_file() and Path(des).exists():shutil.copy(src,des)
                            else:shutil.copytree(src,des,dirs_exist_ok=True,symlinks=True)
                        else:
                            if src=='a':self.list_modes(['shutil.move(fp,des)'],elst,des=des)
                            else:shutil.move(src,des)
                    elif epath=='4':
                        fl=input("Input File/Folder To Delete Or 'a' For Entire List=> ") or '0'
                        if fl=='a':self.list_modes(['Path(fp).unlink()','shutil.rmtree(fp)'],elst)
                        elif Path(fl).is_file():Path(fl).unlink()
                        else:shutil.rmtree(fl)
                    elif epath=='5':Popen([input('Input File To Open=> ')], shell=True)
                    elif epath=='6':self.regex_search(list)
                    elif '.txt' in epath:
                        epath=self.out_dir(epath)
                        with open(epath, 'w', encoding='utf-8') as ep:
                            [ep.write(f'{e}\n') for e in elst]
                    elif epath=='b':break
                    elif epath=='e':self.exit()
                    else:continue
                    if epath!='6':self.get_menu()
            except:pass

    def regex_search(self,list):
        """ [*]Parse Files In List For Regex Pattern:   
    1  ->  Iptv Server Url                   
    2  ->  Ip+Ip:Port                        
    3  ->  Url                               
    4  ->  Mac Address                       
    5  ->  Email:Pass                        
    6  ->  User:Pass                         
    r  ->  Input Regex Pattern  [e.g \S+:\S+]
    b  ->  Back To Previous Screen           
    e  ->  Exit Program                      
"""
        while True:
            self.clear_screen()
            plst=[]
            rgp={
            '1':'h\w+://[\w\-\.]+:?\w+/?\w+?/c',
            '2':'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:?\d{1,5}',
            '3':'\w+://[\w\-\.]+.*$',
            '4':'\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}',
            '5':'[\w\.-]+@[\w\.-]+:[\w\.-]+',
            '6':'^[\w\.-]+:[\w\.-]+$'
            }
            rp=input("\033[1;32;40m"+self.regex_search.__doc__+"\033[0m\nInput Choice=> ") or '0'
            if rp=='b':break
            elif rp=='e':self.exit()
            elif rp[0]=='r':rgp['r']=input('Input Regex Pattern=> ') or None
            if rgp.get(rp):
                for file in list:
                    if Path(file).is_file():
                        with open(file, 'r', encoding="utf8", errors ='replace') as f:
                            [plst.append(a) for b in (x for x in f) for a in re.compile(str(rgp[rp])).findall(b)]
                if plst:self.regex_output(plst)

    def regex_output(self,lst):
        """
 [*]Save Parsed Regex Output To File:                                                 
    File.ext  ->  File To Save Parsed Regex Output  [e.g regex.txt]                   
              ->  Hit Return|Enter Key To Save To Default File  [i.e regex_output.txt]
"""
        self.clear_screen()
        rego=self.out_dir(input("\033[1;32;40m"+self.regex_output.__doc__+"\033[0m\nInput File=> ") or 'regex_output.txt')
        rlst=sorted(set(lst))
        with open(rego, 'w', encoding='utf-8') as out:
            [out.write(f'{r}\n') for r in rlst]
        print("\n\033[1;34;40mTotal►► "+str(len(rlst))+"\033[0m\n\033[1;34;40mOutput►► "+str(rego))
        self.get_menu()
    
    def search_type(self,fpath):
        """
 [*]Search Types [.ext = File Extension Of Choice]:                                                                 
    link.txt ->  Find "link.txt" File                                                                               
    *.ext    ->  Find All Files With .ext File Extension [e.g *.txt Find All Text Files]                            
    test*    ->  Find All Files With Filename Starting With "test" [.ext Optional e.g test*.jpg Files]              
    *test    ->  Find All Files With Filename Ending With "test" [.ext Optional e.g *test.txt Files]                
    *test*   ->  Find All Files With "test" Anywhere In Filename [.ext Optional e.g *test*.py Files]                
    *te*st*  ->  Find All Files With "te" Followed By "st" Anywhere In Filename [.ext Optional e.g *te*st*.py Files]
    b        ->  Back To Input Search Folder                                                                        
    e        ->  Exit Program                                                                                       
             ->  Hit Return To Find All Files In Folder                                                             
"""
        flst=[]
        while True:
            try:
                self.clear_screen()
                stype=input("\033[1;32;40m"+self.search_type.__doc__+"\033[0m\nInput Search Type=> ") or '*'
                if stype=='b':break
                elif stype=='e':self.exit()
                else:
                    flst=list(Path(fpath).rglob(stype))
                    if flst:self.enum_output(flst,fpath)
            except:pass
    
    def exit(self):    
        self.clear_screen()
        kill(getpid(),signal.SIGTERM)
    
    def main(self):
        while True:
            try:
                self.clear_screen()
                fpath=input("\033[1;32;40m"+__doc__+"\033[0m\nInput Search Folder=> ") or path.abspath(sep)
                if Path(fpath).is_dir():self.search_type(fpath)
                elif fpath=='e':self.exit()
            except:pass
        self.clear_screen()

def cli_main():
    Wuddz_Search().main()