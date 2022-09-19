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
 [*]Reddit:    https://reddit.com/user/wuddz-devs                                                     
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
        Path(self.pkg).mkdir(parents=True, exist_ok=True)
    
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
                eout.append(f'{i}  {f}'+' '*4+str(fs)+' '*2+mt)
                me='boss'
            except:pass
            if not me:eout.append(f'{i} {f}')
        total=self.file_size(total)
        eout.append('Total File Size►► '+str(total))
        return eout
    
    def list_archive(self,epath,list,sub,dpl=None,pkk=None):
        try:
            lst=str(self.lf)
            with open(lst, 'w') as bn:
                [bn.write(f'{file}\n') for file in list]
            if dpl!=None:sub=sub.replace(" epath,", " epath, '-spf',")
            out=eval(sub)
            if 'Everything is Ok' in str(out) and dpl==None:
                print("\n\033[1;34;40m['"+str(Path(epath).resolve())+"']► Files Archived Successfully\033[0m")
        except:pass
        Path(lst).unlink()
    
    def list_modes(self,lst,elst,des=None):
        for fp in elst:
            dc=0
            if des!=None:
                fn=Path(fp).name
                while Path(des).joinpath(fn).exists():
                    dc+=1
                    fn=str(Path(fp).stem)+f'_{dc}'+str(Path(fp).suffix)
                dec=str(Path(des).joinpath(fn))
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
                        pkk=''
                        if epath=='1':
                            epath=self.out_dir(input("Input Archive [e.g test.7z]=> ") or str(self.da))
                            if not Path(epath).exists():
                                pkk=getpass("Input Password Or Random Password Used=> ") or None
                                if pkk==None:pkk=''.join(secrets.choice((string.ascii_letters+string.digits).strip()) for i in range(32))
                                sub="run(['7z', 'a', '-t'+str(epath).split('.')[1], epath, '@'+lst, '-mx9', '-p'+pkk], capture_output=True, text=True)"
                                pwf=str(Path(epath).stem)
                                with open(str(self.pf).replace('archive',pwf), 'w') as ps:
                                    ps.write("'"+str(Path(epath).resolve())+"'\n"+str(pkk)+'\n'+'_'*146+'\n\n')
                        else:
                            epath=self.out_dir(epath)
                            if not Path(epath).exists():
                                sub="run(['7z', 'a', '-t'+str(epath).split('.')[1], epath, '@'+lst, '-mx9'], capture_output=True, text=True)"
                        if ndp:self.list_archive(epath,ndp,sub,pkk=pkk)
                        if dup:self.list_archive(epath,dup,sub,dpl='yes')
                    elif epath=='2' or epath=='3':
                        src=input("Input Source File/Folder Or 'a' For Entire List=> ") or None
                        des=input("Input Destination Folder Or Default Folder Used=> ") or self.pkg
                        if epath=='2':
                            if src=='a' and Path(des).is_dir():self.list_modes(['shutil.copy(fp,dec)'],elst,des=des)
                            elif Path(src).is_file():shutil.copy(src,self.out_dir(des))
                            else:shutil.copytree(src,des,dirs_exist_ok=True,symlinks=True)
                        else:
                            if src=='a' and Path(des).is_dir():self.list_modes(['shutil.move(fp,dec)'],elst,des=des)
                            else:shutil.move(src,des)
                    elif epath=='4':
                        fl=input("Input File/Folder To Delete Or 'a' For Entire List=> ") or None
                        if fl=='a':self.list_modes(['Path(fp).unlink()','shutil.rmtree(fp)'],elst)
                        elif Path(fl).is_file():Path(fl).unlink()
                        else:shutil.rmtree(fl)
                    elif epath=='5':
                        fto=input('Input File To Open=> ') or None
                        if fto!=None:
                            if name=='nt':
                                if Path(fto).suffix=='.exe':Popen(['start',str(fto)],shell=True)
                                else:Popen([str(fto)],shell=True)
                            else:Popen(['open '+str(fto)],shell=True)
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
    1  ->  IPTV SERVER URL                   
    2  ->  IP+IP:PORT                        
    3  ->  URL                               
    4  ->  MAC ADDRESS                       
    5  ->  EMAIL:PASS                        
    6  ->  USER:PASS                         
    7  ->  SERVER MAC COMBO                  
    8  ->  M3U URL                           
    r  ->  INPUT REGEX PATTERN  [e.g \S+:\S+]
    b  ->  BACK TO PREVIOUS SCREEN           
    e  ->  EXIT PROGRAM                      
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
            '6':'^[\w\.-]+:[\w\.-]+$',
            '7':'(h\w+://[\w\-\.]+:?\w+/?\w+?/c/)(\s+)?(\S+)?(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})',
            '8':'(h\w+://[\w\-\.]+:?\w+/get.php\?username=\S+?&)(\S+?)?(password=\S+?&)',
            }
            rp=input("\033[1;32;40m"+self.regex_search.__doc__+"\033[0m\nInput Choice=> ") or '0'
            if rp=='b':break
            elif rp=='e':self.exit()
            elif rp[0]=='r':rgp['r']=input('Input Regex Pattern=> ') or None
            if rgp.get(rp):
                for file in list:
                    if Path(file).is_file():
                        with open(file, 'r', encoding="utf8", errors ='replace') as f:
                            if rp=='7':[plst.append(f'{a.group(1)} {a.group(4).upper()}') for b in (x for x in f) for a in re.finditer(str(rgp[rp]),b)]
                            elif rp=='8':[plst.append(f'{a.group(1)}{a.group(3).lower()}') for b in (x for x in f) for a in re.finditer(str(rgp[rp]),b)]
                            else:[plst.append(a) for b in (x for x in f) for a in re.compile(str(rgp[rp])).findall(b)]
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
    
    def main(self):
        while True:
            try:
                self.clear_screen()
                fpath=input("\033[1;32;40m"+__doc__+"\033[0m\nInput Search Folder=> ") or path.abspath(sep)
                if Path(fpath).is_dir():self.search_type(fpath)
                elif fpath=='e':self.exit()
            except:pass
        self.clear_screen()
    
    def exit(self):    
        self.clear_screen()
        kill(getpid(),signal.SIGTERM)


def cli_main():
    wdevs=Wuddz_Search()
    wdevs.main()
