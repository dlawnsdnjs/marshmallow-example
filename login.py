from tkinter import *
from tkinter import ttk
import tkinter
import sys
import os 
from tkinter import messagebox
import tkinter.font
from User import *
from marshmallows import ValidationError
import typing

def signOut():
    signIn()

    # 로그인 실행 함수
    ## 접속 유저 이름 정하는곳.
def signIn():
    idRoot = Tk()
    myId = Login(idRoot)
    idRoot.resizable(0,0)
    idRoot.mainloop()
    myUser = ""
    user = myUser.rstrip('\n')
    
    
    
#close
def on_close(window):
    window.destroy()

#아이디 설정 클래스
class Login:
    def __init__(self, window):
        # 현재 선택된 버튼을 나타냄
        self.selected = ""
        
        # 창을 파괴하기 위한 myParent
        self.myParent = window

        # 제목 표시줄 함수 -> TitleBarSet
        window.title("Sign In")
        
        # x창 눌렀을 때 창 삭제
        self.myParent.protocol("WM_DELETE_WINDOW", lambda:self.on_close(self.myParent))

        # mainFrame은 창 전체를 뜻한다.
        self.mainFrame = Frame(window)
        
        centerWindow(window, 300, 250)
        #window.geometry("250x140")
        self.mainFrame.pack(fill=X)
        self.successCheck = False

        #window.bind("<Return>",self.signInBtn)

        # 내 아이디&비밀번호
        self.myID = ""
        self.myNickname = ""

        #topFrame은 버튼 2개로, 로그인과 회원가입으로 변경할 수 있는 버튼이 있다.
        self.topFrame = Frame(self.mainFrame, background="#1C1C21")

        #topFrame에 들어갈 NavigationFrame
        navigationFrame = Frame(self.topFrame, background="#1E1E1E")

        #centerFrame은 로그인, 회원가입 등의 라벨 등을 출력
        self.centerFrame = Frame(self.mainFrame, width=20, height=200)

        #bottomFrame은 버튼을 놓는 프레임
        self.bottomFrame = Frame(self.mainFrame, background="#EFEFEF")

        self.topFrame.pack(fill=X, side=TOP)
        navigationFrame.pack(fill=X,side=TOP)
        self.centerFrame.pack(fill=BOTH, expand=True)
        self.bottomFrame.pack(fill=X, side=BOTTOM)

        # setting navigation buttons
        self.nav_buttons = {}
        self.nav_buttons['cnt'] = 2
        self.nav_buttons['frame'] = navigationFrame
        self.nav_buttons['list'] = []
        self.nav_buttons['height'] = 3
        self.nav_buttons['width'] = 20
        self.nav_buttons['font'] = tkinter.font.Font(size=20)
        self.nav_buttons['foreground'] = "#FFFFFF"
        self.nav_buttons['background'] = "#1E1E1E"
        self.nav_buttons['activeforeground'] = "#FFFFFF"
        self.nav_buttons['activeforeground'] = "gray15"

        for i in range(self.nav_buttons['cnt']):
            self.nav_buttons['list'].append(Button(self.nav_buttons['frame']))
            self.nav_buttons['list'][i]['foreground'] = "#FFFFFF"
            self.nav_buttons['list'][i]['background'] = "#1E1E1E"
            self.nav_buttons['list'][i]['activeforeground'] = "#FFFFFF"
            self.nav_buttons['list'][i]['activeforeground'] = "gray15"
            self.nav_buttons['list'][i]['width'] = self.nav_buttons['width']
            self.nav_buttons['list'][i]['height'] = self.nav_buttons['height']

        # add navigation Buttons
        self.nav_buttons['list'][0]['text'] = "Sign In"
        self.nav_buttons['list'][1]['text'] = "Sign Up"

        for i in range(self.nav_buttons['cnt']):
            self.nav_buttons['list'][i].pack(side=LEFT)
        
        self.nav_buttons['list'][0]['command'] = lambda:self.sign_in(self.centerFrame)
        self.nav_buttons['list'][1]['command'] = lambda:self.sign_up(self.centerFrame)

        # default = sign_in
        self.sign_in(self.centerFrame)



    # 프레임을 전부 삭제
    def cleanFrame(self, frame):
        self.selected = ""
        # 이론적으로는 pack된 slaves를 destroy
        for i in frame.pack_slaves():
            i.destroy()

    # 로그인 프레임
    def sign_in(self, frame):
        if self.selected != "sign_in":
            self.cleanFrame(frame)
            self.selected = "sign_in"

            # ID를 담는 라벨
            self.idFrame = Frame(frame)
            self.idFrame.pack(expand=True,pady=5)
            self.idLabel = Label(self.idFrame,text="ID : ")
            self.idText = Entry(self.idFrame)
            self.idText.icursor(0)
            self.idText.focus_set()
            self.idLabel.pack(side=LEFT, ipadx = 13)
            self.idText.pack(side=RIGHT, padx = 20)

            # pw를 담는 라벨
            self.passwdFrame = Frame(frame)
            self.passwdFrame.pack(pady=5)
            self.passwdLabel = Label(self.passwdFrame,text = "Password : ")
            self.passwdText = Entry(self.passwdFrame,show="*")
            self.passwdLabel.pack(side=LEFT)
            self.passwdText.pack(side=RIGHT, padx=20)

            # 로그인 데이터 체크 버튼
            self.loginDataFrame = Frame(frame)
            self.loginDataFrame.pack(pady=5)
            self.login_check = BooleanVar()

            self.loginData = tkinter.Checkbutton(self.loginDataFrame, text="Stay signed in",variable=self.login_check)
            self.loginData.deselect()
            self.loginData.pack(side=BOTTOM, padx=20)

            self.loginButton = Button(frame,text="Sign in", command=self.signInBtn)
            #엔터키랑 연동
            self.myParent.bind('<Return>',self.signInBtn)
            self.loginButton.pack(pady=10)

    # 회원가입 프레임
    def sign_up(self, frame):
        if self.selected != "sign_up":
            self.cleanFrame(frame)
            self.selected = "sign_up"
            self.myParent.bind("<Return>",self.signUpBtn)

            # ID를 입력하는 라벨
            self.idFrame = Frame(frame)
            self.idFrame.pack(expand=True, pady=5)
            self.idLabel = Label(self.idFrame,text="ID : ")
            self.idText = Entry(self.idFrame)
            self.idText.icursor(0)
            self.idText.focus_set()
            self.idLabel.pack(side=LEFT, ipadx = 13)
            self.idText.pack(side=RIGHT, padx = 20)

            # 비밀번호를 입력하는 라벨
            self.passwdFrame = Frame(frame)
            self.passwdFrame.pack(pady = 5)
            self.passwdLabel = Label(self.passwdFrame,text = "Password : ")
            self.passwdText = Entry(self.passwdFrame,show="*")
            self.passwdLabel.pack(side=LEFT)
            self.passwdText.pack(side=RIGHT, padx=20)

            # 닉네임을 입력하는 라벨
            self.nicknameFrame = Frame(frame)
            self.nicknameFrame.pack(pady = 5)
            self.nicknameLabel = Label(self.nicknameFrame, text="Nickname : ")
            self.nicknameText = Entry(self.nicknameFrame)
            self.nicknameLabel.pack(side=LEFT)
            self.nicknameText.pack(side=RIGHT, padx=20)

            # 가입 요청을 하는 버튼
            self.requestButton = Button(frame, text="Sign Up",command=self.signUpBtn)
            self.requestButton.pack(pady = 10)


    # 회원가입 요청을 하였을 때 실행
    def signUpBtn(self, event=None):
        # 빈 문자열인지 확인
        if (len(self.idText.get())!= 0) and (len(self.passwdText.get()) != 0) and (len(self.nicknameText.get()) != 0):
            self.createID()

    def exitBtn(self, window, event=None):
        window.destroy()

    # id를 생성
    def createID(self):
        # 파일 데이터 생성
        #################### 필독 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # id와 패스워드와 닉네임이 사용가능한 문자열인지 무조건 확인 필요.(에러 예방)
        user = User(self.idText.get(), self.passwdText.get(), self.nicknameText.get())
        schema = UserSchema()
        result = schema.dumps(user) # user를 json 형식으로 직렬화(타입은 str)
        re = schema.dump(user) # user를 dict 형식으로 직렬화
        
        try:
            re_value = re.values() 
            for v in re_value: # userID, userPW, userNN에 대한 유효성 검사를 실시한다.
                if(v == re["created_at"]):
                    break
                validator(v)
                print(v)
            if os.path.isfile("register.json"): # 생성하려는 아이디가 중복되지 않는지 검사한다.
                with open("register.json", "r") as f:
                    while True:
                        row = f.readline()
                        print(type(row))
                        print(row)
                        if not row:
                            break
                        temp = schema.loads(row)
                        if(temp["userID"] == re["userID"]):
                            raise ValidationError("중복되는 아이디입니다.")
                                
            with open("register.json", "a") as f: # 생성한 아이디 정보를 파일에 저장한다.
                f.writelines(result)
                f.write("\n")
                messagebox.showinfo('Success!','Success in Sign Up')
        except ValidationError as err:
            messagebox.showerror('Fail!1',typing.cast(typing.Dict[str, typing.List[str]], err.messages))
            # 유효성 검사나 아이디 중복 검사에서 발생한 에러를 새 창에 출력한다.

        
    def on_close(self, window):
        window.destroy()


    # 로그인 실행
    def signInCheck(self):
        user = User(self.idText.get(), self.passwdText.get())
        schema = UserSchema()
        result = schema.dumps(user)
        re = schema.dump(user)
        try:
            re_value = re.values()
            for v in re_value: # userID, userPW에 대한 유효성 검사를 실시한다.
                if(v == re["userNN"]):
                    break
                validator(v)
            with open("register.json", "r") as f: # 입력한 아이디에 대한 정보 탐색
                while True:
                    row = f.readline()
                    if not row:
                        break
                    temp = schema.loads(row)
                    if(temp["userID"] == re["userID"]):
                        if(temp["userPW"] == re["userPW"]): # 아이디와 패스워드 모두 일치할 경우 로그인 성공
                            messagebox.showinfo('Success!','로그인 성공!')
                            return
                        else:
                            messagebox.showinfo('Fail', '비밀번호가 틀렸습니다.')
                            return
                self.loginFailed()
                # 아이디나 패스워드의 형식은 만족하나 일치하는 아이디가 없을 경우 로그인 실패 메시지를 출력한다.
        except Exception as err:
            messagebox.showerror('Fail!1',typing.cast(typing.Dict[str, typing.List[str]], err.messages))
            # 입력한 아이디나 패스워드의 형식이 맞지 않는 경우 발생한 에러를 새 창에 출력한다.

    # 로그인 실패
    def loginFailed(self):
        printstr = '로그인 실패'
        messagebox.showinfo(printstr,printstr)


    # 로그인 버튼 -> 로그인 체크만 수행한다.
    def signInBtn(self, event=None):
            self.signInCheck()


    # 창을 정 중앙에 위치
def centerWindow(window ,width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = screen_width/2 - width/2
        y = screen_height/2 - height/2
        window.geometry('%dx%d+%d+%d' %(width,height,x,y))
        
signIn()