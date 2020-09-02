import asyncio
import discord
import datetime
import threading
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("상태메시지")
    await client.change_presence(status=discord.Status.online, activity=game)


#빅마변수(bigma)
bigmaTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_bigmaTime = datetime.datetime.now()+datetime.timedelta(days=365)
bigmaTimeString = '99:99:99'
tmp_bigmaTimeString = ''
bigmaFlag = False
     
#우크변수(wook)
wookTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_wookTime = datetime.datetime.now()+datetime.timedelta(days=365)
wookTimeString = '99:99:99'
tmp_wookTimeString = ''
wookFlag = False
    
#마녀변수(manyeo)
manyeoTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_manyeoTime = datetime.datetime.now()+datetime.timedelta(days=365)
manyeoTimeString = '99:99:99'
tmp_manyeoTimeString = ''
manyeoFlag = False

#바슬변수(basle)
basleTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_basleTime = datetime.datetime.now()+datetime.timedelta(days=365)
basleTimeString = '99:99:99'
tmp_basleTimeString = ''
basleFlag = False

#칼리고변수(caligo)
caligoTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_caligoTime = datetime.datetime.now()+datetime.timedelta(days=365)
caligoTimeString = '99:99:99'
tmp_caligoTimeString = ''
caligoFlag = False

#우헤헤(파)변수(blue3)
blue3Time = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_blue3Time = datetime.datetime.now()+datetime.timedelta(days=365)
blue3TimeString = '99:99:99'
tmp_blue3TimeString = ''
blue3Flag = False

#이히히(빨)변수(red3)
red3Time = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_red3Time = datetime.datetime.now()+datetime.timedelta(days=365)
red3TimeString = '99:99:99'
tmp_red3TimeString = ''
red3Flag = False

#우히힉(초)변수(green3)
green3Time = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_green3Time = datetime.datetime.now()+datetime.timedelta(days=365)
green3TimeString = '99:99:99'
tmp_green3TimeString = ''
green3Flag = False

#깬쿠변수(sleep2)
sleep2Time = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_sleep2Time = datetime.datetime.now()+datetime.timedelta(days=365)
sleep2TimeString = '99:99:99'
tmp_sleep2TimeString = ''
sleep2Flag = False

#가임변수(imp4)
imp4Time = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_imp4Time = datetime.datetime.now()+datetime.timedelta(days=365)
imp4TimeString = '99:99:99'
tmp_imp4TimeString = ''
imp4Flag = False

#데블랑변수(devil5)
devil5Time = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_devil5Time = datetime.datetime.now()+datetime.timedelta(days=365)
devil5TimeString = '99:99:99'
tmp_devil5TimeString = ''
devil5Flag = False

#은둔자변수(hider)
hiderTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_hiderTime = datetime.datetime.now()+datetime.timedelta(days=365)
hiderTimeString = '99:99:99'
tmp_hiderTimeString = ''
hiderFlag = False

#블랙스컬(black1)
black1Time = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_black1Time = datetime.datetime.now()+datetime.timedelta(days=365)
black1TimeString = '99:99:99'
tmp_black1TimeString = ''
black1Flag = False
    
#해변자라변수(hzara)
hzaraTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_hzaraTime = datetime.datetime.now()+datetime.timedelta(days=365)
hzaraTimeString = '99:99:99'
tmp_hzaraTimeString = ''
hzaraFlag = False

#등섬자라변수(dzara)
dzaraTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_dzaraTime = datetime.datetime.now()+datetime.timedelta(days=365)
dzaraTimeString = '99:99:99'
tmp_dzaraTimeString = ''
dzaraFlag = False

#탱크변수(tank)
tankTime = datetime.datetime.now()+datetime.timedelta(days=365)
tmp_tankTime = datetime.datetime.now()+datetime.timedelta(days=365)
tankTimeString = '99:99:99'
tmp_tankTimeString = ''
tankFlag = False


@client.event
async def on_message(message):
    if message.content.startswith("!도움말"):
        embed = discord.Embed(title="안녕하세요. 제작자 < 흥> 입니다.", description="``명령어 목록``에 대해 설명해 드리겠습니다.\n해당 봇은 명령어``!``를 기본으로 합니다.", color=0x62c1cc)
        embed.add_field(name="■  보스 명령어", value="``!보스탐``\n``!<보스이름> 컷``  (현재시간 자동등록)\n``!<보스이름> 컷 hh:mm:ss``  (컷시간 수동등록)\n``!보스탐초기화``", inline=False)
        embed.add_field(name="<보스이름>", value="``빅마`` ``우크`` ``마녀`` ``바슬`` ``칼리고``\n``블스`` ``은둔`` ``깬쿠`` ``빨`` ``파`` ``초`` ``가임`` ``데블랑``\n``등던자라`` ``해변자라`` ``탱크`` \n``+ 원하시는거 추가해드립니다``", inline=False)
        embed.add_field(name="■  지도 명령어", value="``!지도 <맵이름>``", inline=False)
        embed.add_field(name="<맵이름>", value="``등던1`` ``등던2`` ``등던3`` ``등던4`` ``등던5``\n ``노을숲`` ``카타르`` ``라평`` ``폐숲`` ``중사`` ``제사`` ``왕사``\n``누각`` ``동`` ``서`` ``요새`` ``미로`` ``타신``\n``미궁`` ``에이존`` ``비존``\n``시프넬`` ``세레인`` ``오통`` ``실험실`` ``신전``", inline=False)
        await message.channel.send(embed=embed)

    if message.content == "!지도 등던1":
        embed = discord.Embed(title="아이모 지도", description="등대던전1F", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690114476858671157/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 등던2":
        embed = discord.Embed(title="아이모 지도", description="등대던전2F", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690115502802206776/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 등던3":
        embed = discord.Embed(title="아이모 지도", description="등대던전3F", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690117554408128698/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 등던4":
        embed = discord.Embed(title="아이모 지도", description="등대던전4F", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690118589369286656/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 등던5":
        embed = discord.Embed(title="아이모 지도", description="등대던전5F", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690121187765911613/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 시프넬":
        embed = discord.Embed(title="아이모 지도", description="시프넬의 길", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690214556093775931/1584630051656.jpg")
        await message.channel.send(embed=embed)
    if message.content == "!지도 세레인":
        embed = discord.Embed(title="아이모 지도", description="세레인의 제단", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690199445077622942/1584620311554.jpg")
        await message.channel.send(embed=embed)
    if message.content == "!지도 오통":
        embed = discord.Embed(title="아이모 지도", description="세레인의 제단", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690206743602397283/1584628485501.jpg")
        await message.channel.send(embed=embed)
    if message.content == "!지도 실험실":
        embed = discord.Embed(title="아이모 지도", description="이슬롯의 실험실", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690199444657930292/1584620312843.jpg")
        await message.channel.send(embed=embed)
    if message.content == "!지도 신전":
        embed = discord.Embed(title="아이모 지도", description="이슬롯의 신전", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690205853675946041/1584628281609.jpg")
        await message.channel.send(embed=embed)
    if message.content == "!지도 중사":
        embed = discord.Embed(title="아이모 지도", description="뜨거운 모래사막", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690215714170077197/20200320_001028.jpg")
        await message.channel.send(embed=embed)
    if message.content == "!지도 제사":
        embed = discord.Embed(title="아이모 지도", description="모래무덤 골짜기", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690215713901903961/20200320_001010.jpg")
        await message.channel.send(embed=embed)
    if message.content == "!지도 왕사":
        embed = discord.Embed(title="아이모 지도", description="건조한 초원", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690237144459247788/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 미궁":
        embed = discord.Embed(title="아이모 지도", description="숲의 미궁", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690206744542052598/1584628323763.jpg")
        await message.channel.send(embed=embed)
    if message.content == "!지도 에이존":
        embed = discord.Embed(title="아이모 지도", description="숲의 미궁-좌수정", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690206745070665733/1584628312902.jpg")
        await message.channel.send(embed=embed)
    if message.content == "!지도 비존":
        embed = discord.Embed(title="아이모 지도", description="숲의 미궁-우수정", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690206745611599900/1584628315136.jpg")
        await message.channel.send(embed=embed)
    if message.content == "!지도 노을숲":
        embed = discord.Embed(title="아이모 지도", description="해지는 노을숲", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690394301972086784/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 카타르":
        embed = discord.Embed(title="아이모 지도", description="카타르 산맥", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690394362252623903/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 라평":
        embed = discord.Embed(title="아이모 지도", description="라노스 평원", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690396309428895754/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 폐숲":
        embed = discord.Embed(title="아이모 지도", description="폐허가 있는 숲", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690398247210057748/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 누각":
        embed = discord.Embed(title="아이모 지도", description="고대의 누각", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690403680394149907/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 동":
        embed = discord.Embed(title="아이모 지도", description="하늘성채-동부", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690404996759683082/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 서":
        embed = discord.Embed(title="아이모 지도", description="하늘성채-서부", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690404330938957844/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 미로":
        embed = discord.Embed(title="아이모 지도", description="알수없는 미로", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690405502571773952/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 요새":
        embed = discord.Embed(title="아이모 지도", description="돌무더기 요새", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690405251383164978/unknown.png")
        await message.channel.send(embed=embed)
    if message.content == "!지도 타신":
        embed = discord.Embed(title="아이모 지도", description="타락한 신전", color=0x62c1cc) 
        embed.set_image(url="https://cdn.discordapp.com/attachments/690096795723759679/690405976041324614/unknown.png")
        await message.channel.send(embed=embed)


    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.
    
    global channel
    global nowTimeString

    #빅마변수지정
    global bigmaTime
    global bigmaTimeString
    global tmp_bigmaTimeString
    global bigmaFlag

    #우크변수지정
    global wookTime
    global wookTimeString
    global tmp_wookTimeString
    global wookFlag

    #마녀변수지정
    global manyeoTime
    global manyeoTimeString
    global tmp_manyeoTimeString
    global manyeoFlag

    #바슬변수지정
    global basleTime
    global basleTimeString
    global tmp_basleTimeString
    global basleFlag

    #칼리고변수지정
    global caligoTime
    global caligoTimeString
    global tmp_caligoTimeString
    global caligoFlag

    #우헤헤(파)변수지정
    global blue3Time
    global blue3TimeString
    global tmp_blue3TimeString
    global blue3Flag

    #이히히(빨)변수지정
    global red3Time
    global red3TimeString
    global tmp_red3TimeString
    global red3Flag

    #우히힉(초)변수지정
    global green3Time
    global green3TimeString
    global tmp_green3TimeString
    global green3Flag

    #잠깬쿠이변수지정
    global sleep2Time
    global sleep2TimeString
    global tmp_sleep2TimeString
    global sleep2Flag

     #가디언임프변수지정
    global imp4Time
    global imp4TimeString
    global tmp_imp4TimeString
    global imp4Flag

     #데블랑 변수지정
    global devil5Time
    global devil5TimeString
    global tmp_devil5TimeString
    global devil5Flag

     #은둔자변수지정
    global hiderTime
    global hiderTimeString
    global tmp_hiderTimeString
    global hiderFlag

     #블랙스컬변수지정
    global black1Time
    global black1TimeString
    global tmp_black1TimeString
    global black1Flag

     #해변자라변수지정
    global hzaraTime
    global hzaraTimeString
    global tmp_hzaraTimeString
    global hzaraFlag

     #등섬자라변수지정
    global dzaraTime
    global dzaraTimeString
    global tmp_dzaraTimeString
    global dzaraFlag

     #탱크변수지정
    global tankTime
    global tankTimeString
    global tmp_tankTimeString
    global tankFlag



    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    modify = ''
    try:
        hello = message.content
        length = len(hello)     # UTF-8로 인코딩 했을 때 바이트 수를 구함
        print(hello)
        print(length)
    
        if length == 13:
            hours = hello[5:7]
            minutes = hello[8:10]
            seconds = hello[11:13]
            now = datetime.datetime.now()
            now = now.replace(hour=int(hours), minute=int(minutes), second=int(seconds))
        elif length == 14:
            hours = hello[6:8]
            minutes = hello[9:11]
            seconds = hello[12:14]
            now = datetime.datetime.now()
            now = now.replace(hour=int(hours), minute=int(minutes), second=int(seconds))
        elif length == 15:
            hours = hello[7:9]
            minutes = hello[10:12]
            seconds = hello[13:15]
            now = datetime.datetime.now()
            now = now.replace(hour=int(hours), minute=int(minutes), second=int(seconds))
        elif length == 16:
            hours = hello[8:10]
            minutes = hello[11:13]
            seconds = hello[14:16]
            now = datetime.datetime.now()
            now = now.replace(hour=int(hours), minute=int(minutes), second=int(seconds))
        else :
            now = datetime.datetime.now()
            nowTimeString = now.strftime('%H:%M:%S')

    except:
        print('exception');
        now = datetime.datetime.now()
        nowTimeString = now.strftime('%H:%M:%S')
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ컷명령어ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    
    if message.content.startswith('!빅마 컷'):
        bigmaFlag = False
        bigmaTime = nextTime = now+datetime.timedelta(hours=20)+datetime.timedelta(minutes=55)+datetime.timedelta(seconds=0)
        tmp_bigmaTimeString = bigmaTimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 빅마 ' + bigmaTimeString + '\n---(젠타임 20:55:00 적용)  \n※참고사항--1젠만 15분 길어요.\n1젠21:05:00```')

    if message.content.startswith('!우크 컷'):
        wookFlag = False
        wookTime = nextTime = now+datetime.timedelta(hours=20)+datetime.timedelta(minutes=57)+datetime.timedelta(seconds=0)
        tmp_wookTimeString = wookTimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 우크 ' + wookTimeString + '\n---(젠타임 20:57:00 적용)  \n※참고사항--1젠만 18분 길어요.\n1젠21:15:00```')

    if message.content.startswith('!마녀 컷'):
        manyeoFlag = False
        manyeoTime = nextTime = now+datetime.timedelta(hours=48)+datetime.timedelta(minutes=00)+datetime.timedelta(seconds=0)
        tmp_manyeoTimeString = manyeoTimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 마녀 ' + manyeoTimeString + '\n---(젠타임 48:00:00 적용)```')

    if message.content.startswith('!바슬 컷'):
        basleFlag = False
        basleTime = nextTime = now+datetime.timedelta(hours=22)+datetime.timedelta(minutes=20)+datetime.timedelta(seconds=0)
        tmp_basleTimeString = basleTimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 바슬 ' + basleTimeString + '\n---(젠타임 22:20:00 적용)```')

    if message.content.startswith('!칼리고 컷'):
        caligoFlag = False
        caligoTime = nextTime = now+datetime.timedelta(hours=0)+datetime.timedelta(minutes=0)+datetime.timedelta(seconds=1)
        tmp_caligoTimeString = caligoTimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n 고생하셨습니다. 칼리고 ' + caligoTimeString + '컷 다음주에 또 잡아요! \n---(젠타임 168:00:00 적용)```')

    if message.content.startswith('!파 컷'):
        blue3Flag = False
        blue3Time = nextTime = now+datetime.timedelta(hours=1)+datetime.timedelta(minutes=5)+datetime.timedelta(seconds=20)
        tmp_blue3TimeString = blue3TimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 우헤헤(파) ' + blue3TimeString + '\n---(젠타임 01:05:20 적용)```')

    if message.content.startswith('!빨 컷'):
        red3Flag = False
        red3Time = nextTime = now+datetime.timedelta(hours=1)+datetime.timedelta(minutes=6)+datetime.timedelta(seconds=50)
        tmp_red3TimeString = red3TimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 이히히(빨) ' + red3TimeString + '\n---(젠타임 01:06:50 적용)```')

    if message.content.startswith('!초 컷'):
        green3Flag = False
        green3Time = nextTime = now+datetime.timedelta(hours=1)+datetime.timedelta(minutes=8)+datetime.timedelta(seconds=30)
        tmp_green3TimeString = green3TimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 우히힉(초) ' + green3TimeString + '\n---(젠타임 01:08:30 적용)```')

    if message.content.startswith('!깬쿠 컷'):
        sleep2Flag = False
        sleep2Time = nextTime = now+datetime.timedelta(hours=1)+datetime.timedelta(minutes=3)+datetime.timedelta(seconds=30)
        tmp_sleep2TimeString = sleep2TimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 잠깬쿠이 ' + sleep2TimeString + '\n---(젠타임 01:03:30 적용)```')

    if message.content.startswith('!가임 컷'):
        imp4Flag = False
        imp4Time = nextTime = now+datetime.timedelta(hours=1)+datetime.timedelta(minutes=3)+datetime.timedelta(seconds=0)
        tmp_imp4TimeString = imp4TimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 가디언임프 ' + imp4TimeString + '\n---(젠타임 01:03:00 적용)```')

    if message.content.startswith('!데블랑 컷'):
        devil5Flag = False
        devil5Time = nextTime = now+datetime.timedelta(hours=5)+datetime.timedelta(minutes=33)+datetime.timedelta(seconds=33)
        tmp_devil5TimeString = devil5TimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 데블랑 ' + devil5TimeString + '\n---(젠타임 05:33:33 적용) \n※참고사항--1젠만 10분 길어요.\n1젠05:43:00```')

    if message.content.startswith('!은둔 컷'):
        hiderFlag = False
        hiderTime = nextTime = now+datetime.timedelta(hours=11)+datetime.timedelta(minutes=23)+datetime.timedelta(seconds=0)
        tmp_hiderTimeString = hiderTimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 은둔자 ' + hiderTimeString + '\n---(젠타임 11:23:00 적용)```')

    if message.content.startswith('!블스 컷'):
        black1Flag = False
        black1Time = nextTime = now+datetime.timedelta(hours=0)+datetime.timedelta(minutes=57)+datetime.timedelta(seconds=0)
        tmp_black1TimeString = black1TimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 블랙스컬 ' + black1TimeString + '\n---(젠타임 00:57:00 적용)```')

    if message.content.startswith('!탱크 컷'):
        tankFlag = False
        tankTime = nextTime = now+datetime.timedelta(hours=0)+datetime.timedelta(minutes=58)+datetime.timedelta(seconds=20)
        tmp_tankTimeString = tankTimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 탱크 ' + tankTimeString + '\n---(젠타임 00:58:20 적용)```')

    if message.content.startswith('!해변자라 컷'):
        hzaraFlag = False
        hzaraTime = nextTime = now+datetime.timedelta(hours=5)+datetime.timedelta(minutes=33)+datetime.timedelta(seconds=0)
        tmp_hzaraTimeString = hzaraTimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 해변자라 ' + hzaraTimeString + '\n---(젠타임 05:33:00 적용) \n※참고사항--1~4젠은 직접계산하세요.\n1젠06:50:00\n2젠06:30:00\n3젠06:10:00\n4젠05:50:00\n5젠 젠타임 동일```')

    if message.content.startswith('!등섬자라 컷'):
        dzaraFlag = False
        dzaraTime = nextTime = now+datetime.timedelta(hours=20)+datetime.timedelta(minutes=30)+datetime.timedelta(seconds=0)
        tmp_dzaraTimeString = dzaraTimeString = nextTime.strftime('%H:%M:%S')
        await message.channel.send('```diff\n다음 등섬자라 ' + dzaraTimeString + '\n---(젠타임 68:30:00 적용) \n※참고사항--젠마다 젠타임3:30분씩 줄어듬\n1젠68:30:00\n2젠65:00:00\n3젠61:30:00\n4젠58:00:00```')

 
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ불러오기ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    if message.content.startswith('!불러오기'):
        file = open("E:\my_bot.db", 'r')
        
        while True:
            line = file.readline();
            
            if not line: break
            
            #await message.channel.send(line)
            
            if (line.startswith(' - 빅마 : ')):
                hours = line[8:10]
                minutes = line[11:13]
                now2 = datetime.datetime.now()
                now2 = now.replace(hour=int(hours), minute=int(minutes))
                bigmaTime = now2
                bigmaTimeString = bigmaTime.strftime('%H:%M:%S')
        file.close()
        await message.channel.send('불러오기 완료')
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ클리어ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    if message.content.startswith("!보스탐초기화"):
        bigmaTimeString = '99:99:99'
        wookTimeString = '99:99:99'
        manyeoTimeString = '99:99:99'
        basleTimeString = '99:99:99'
        caligoTimeString = '99:99:99'
        black1TimeString = '99:99:99'
        hiderTimeString = '99:99:99'
        sleep2TimeString = '99:99:99'
        red3TimeString = '99:99:99'
        blue3TimeString = '99:99:99'
        green3TimeString = '99:99:99'
        imp4TimeString = '99:99:99'
        devil5TimeString = '99:99:99'
        dzaraTimeString = '99:99:99'
        hzaraTimeString = '99:99:99'
        tankTimeString = '99:99:99'
   
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ대형보스ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    if message.content.startswith("!보스탐"):
        mainlist=[bigmaTimeString,wookTimeString,manyeoTimeString,basleTimeString,caligoTimeString]
        information= '\n---  ■ 대형보스\n'

        for timestring in mainlist:
            #print(timestring)
        
            if timestring == bigmaTimeString:
                if bigmaTimeString != '99:99:99':
                    information += '    - 빅마 : ' + bigmaTimeString +'\n'
            if timestring == wookTimeString:
                if wookTimeString != '99:99:99':
                    information += '    - 우크 : ' + wookTimeString + '\n'
            if timestring == manyeoTimeString:
                if manyeoTimeString != '99:99:99':
                    information += '    - 마녀 : ' + manyeoTimeString +'\n'
            if timestring == basleTimeString:
                if basleTimeString != '99:99:99':
                    information += '    - 바슬 : ' + basleTimeString +'\n'
            if timestring == caligoTimeString:
                if caligoTimeString != '99:99:99':
                    information += '    - 칼리고 : ' + caligoTimeString +' 이번주 컷\n'


        if bigmaTimeString == '99:99:99':
                    information += '    - 빅마 : '+'입력 정보 없음 '+'\n'
        if wookTimeString == '99:99:99':
                    information += '    - 우크 : '+'입력 정보 없음 '+'\n'
        if manyeoTimeString == '99:99:99':
                    information += '    - 마녀 : '+'입력 정보 없음 '+'\n'
        if basleTimeString == '99:99:99':
                    information += '    - 바슬 : '+'입력 정보 없음 '+'\n'
        if caligoTimeString == '99:99:99':
                    information += '    - 칼리고 : '+'입력 정보 없음 '+'\n'


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ등던보스ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        lighthouselist=[blue3TimeString,red3TimeString,green3TimeString,sleep2TimeString,imp4TimeString,black1TimeString,hiderTimeString,devil5TimeString]
        lighthouseboss= '\n---  ■ 등던보스\n'

        for timestring in lighthouselist:
            #print(timestring)

            if timestring == hiderTimeString:
                if hiderTimeString != '99:99:99':
                    lighthouseboss += '    - 은둔자 : ' + hiderTimeString +'\n'
            if timestring == black1TimeString:
                if black1TimeString != '99:99:99':
                    lighthouseboss += '    - 블랙스컬 : ' + black1TimeString +'\n'
            if timestring == sleep2TimeString:
                if sleep2TimeString != '99:99:99':
                    lighthouseboss += '    - 잠깬쿠이 : ' + sleep2TimeString +'\n'
            if timestring == blue3TimeString:
                if blue3TimeString != '99:99:99':
                    lighthouseboss += '    - 우헤헤(파) : ' + blue3TimeString +'\n'
            if timestring == red3TimeString:
                if red3TimeString != '99:99:99':
                    lighthouseboss += '    - 이히히(빨) : ' + red3TimeString +'\n'
            if timestring == green3TimeString:
                if green3TimeString != '99:99:99':
                    lighthouseboss += '    - 우히힉(초) : ' + green3TimeString +'\n'
            if timestring == imp4TimeString:
                if imp4TimeString != '99:99:99':
                    lighthouseboss += '    - 가디언임프 : ' + imp4TimeString +'\n'
            if timestring == devil5TimeString:
                if devil5TimeString != '99:99:99':
                    lighthouseboss += '    - 데블랑 : ' + devil5TimeString +'\n'


        if hiderTimeString == '99:99:99':
                    lighthouseboss += '    - 은둔자 : '+'입력 정보 없음 '+'\n'
        if black1TimeString == '99:99:99':
                    lighthouseboss += '    - 블랙스컬 : '+'입력 정보 없음 '+'\n'
        if sleep2TimeString == '99:99:99':
                    lighthouseboss += '    - 잠깬쿠이 : '+'입력 정보 없음 '+'\n'
        if blue3TimeString == '99:99:99':
                    lighthouseboss += '    - 우헤헤(파) : '+'입력 정보 없음 '+'\n'
        if red3TimeString == '99:99:99':
                    lighthouseboss += '    - 이히히(빨) : '+'입력 정보 없음 '+'\n'
        if green3TimeString == '99:99:99':
                    lighthouseboss += '    - 우히힉(초) : '+'입력 정보 없음 '+'\n'
        if imp4TimeString == '99:99:99':
                    lighthouseboss += '    - 가디언임프 : '+'입력 정보 없음 '+'\n'
        if devil5TimeString == '99:99:99':
                    lighthouseboss += '    - 데블랑 : '+'입력 정보 없음 '+'\n'

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ세미ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        fieldlist=[hzaraTimeString,dzaraTimeString,tankTimeString]
        fieldboss= '\n---  ■ 필드보스\n'

        for timestring in fieldlist:
            #print(timestring)

            if timestring == hzaraTimeString:
                if hzaraTimeString != '99:99:99':
                    fieldboss += '    - 해변자라 : ' + hzaraTimeString +'\n'
            if timestring == dzaraTimeString:
                if dzaraTimeString != '99:99:99':
                    fieldboss += '    - 등던자라 : ' + dzaraTimeString +'\n'
            if timestring == tankTimeString:
                if tankTimeString != '99:99:99':
                    fieldboss += '    - 탱크 : ' + tankTimeString +'\n'


        if hzaraTimeString == '99:99:99':
                    fieldboss += '    - 해변자라 : '+'입력 정보 없음 '+'\n'
        if dzaraTimeString == '99:99:99':
                    fieldboss += '    - 등던자라 : '+'입력 정보 없음 '+'\n'
        if tankTimeString == '99:99:99':
                    fieldboss += '    - 탱크 : '+'입력 정보 없음 '+'\n'
        

        await message.channel.send('```diff\n-- ━━━━━━━━━━ 보스 타임 정보 ━━━━━━━━━━ ' + information + lighthouseboss + fieldboss +'-- ━━━━━━━━━━━━━━━━━━━━━━━━━━━━```')

        file = open("E:\my_bot.db", 'w')
        file.write(information);
        file.close()

access_token = os.environ["BOT_TOKEN"]        
client.run(access_token)
