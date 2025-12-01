import tkinter  # 导入Tkinter主模块
import random   # 用于随机选择祝福语和颜色
import time     # 控制动画时间间隔
import pygame   # 用于播放音乐
import sys      # 用于系统路径操作
import os       # 用于路径操作

"""
    一键弹出多个祝福语窗口的python脚本
"""

class BlessingPopup:
    def __init__(self):
        # 创建主窗口（但不显示），作为弹窗的寄生容器
        self.root = tkinter.Tk()
        self.root.overrideredirect(True)   # 移除窗口边框和标题栏
        self.root.attributes('-alpha', 0)   # 设置主窗口完全透明，避免显示
        self.root.attributes('-topmost', True) # 窗口始终置顶
        
        # 数据源：祝福语列表（增加到100条）和颜色列表
        self.blessings = [
            "多喝水哦~", "温馨提示", "保持好心情", "我想你了",
            "祝你开心每一天", "记得按时吃饭", "今天你很棒", "加油，你可以的",
            "休息一下吧", "笑口常开", "每一天都是新的开始", "你值得最好的",
            "愿你有个美好的一天", "相信自己", "别忘记微笑", "放松一下",
            "感谢有你", "慢慢来，不着急", "照顾好自己", "你真的很不错",
            "今天也要加油鸭", "每一天都很美好", "相信明天会更好", "给自己一个拥抱",
            "享受当下的每一刻", "你比想象中更强大", "坚持就是胜利", "快乐最重要",
            "记得深呼吸", "世界因你而美好", "勇敢做自己", "简单就是幸福",
            "保持好奇心", "学会感恩", "今天的努力不会白费", "记得奖励自己",
            "做喜欢的事", "珍惜每一个瞬间", "你的笑容很治愈", "给自己一点空间",
            "相信直觉", "慢慢来，比较快", "你已经做得很好了", "生活总有惊喜",
            "谢谢你的善良", "多和朋友联系", "享受阳光", "今天也要对自己温柔一点", "累了就歇歇，别太拼", "你的感受我都懂", "生活需要慢慢品味",
            "记得要好好吃饭", "简单快乐就很棒", "平凡的日子也很温暖", "进步一点点就很好",
            "给生活加点甜", "今天也要开心呀", "笑一笑，心情好", "你真的超棒的",
            "今天也要好好过", "你已经很优秀了", "笑起来真好看", "一切都会慢慢变好",
            "给自己鼓鼓掌", "慢慢来，不着急", "享受当下的美好", "乐观一点，生活更美",
            "你是最特别的", "未来可期", "每天都有小进步", "梦想会实现的",
            "健康最重要", "跑跑步，吹吹风", "早点休息对身体好", "养成好习惯",
            "好好爱自己", "珍惜眼前人", "感谢生活中的小确幸", "谦逊是美德",
            "累了就休息一下", "今天也要好好爱自己", "你的感受很重要", "别给自己太多压力",
            "你已经很努力了", "给自己一个温暖的拥抱", "记得对自己好一点", "你的存在就是美好",
            "今天也要好好喝水", "累了就停下来歇歇", "你的心情我理解", "别太勉强自己",
            "今天也要好好睡觉", "你的努力我都看在眼里", "累了就来抱抱", "你已经很棒了",
            "今天也要好好照顾自己", "你的付出值得被看见", "累了就靠在我肩上", "别给自己太大压力",
            "今天也要好好放松", "你的笑容很珍贵", "累了就来聊聊天", "你已经做得很好了",
            "今天也要好好呼吸", "你的存在很有意义", "累了就听听音乐", "别太苛责自己"
        ]
        self.colors = ['#FFB6C1', '#87CEFA', '#98FB98', '#DDA0DD', '#FFFFE0', '#FFA500', '#9370DB', '#3CB371']

    # 创建弹窗
    def create_popup(self):
        # 随机选择祝福语和背景色
        blessing = random.choice(self.blessings)
        color = random.choice(self.colors)
        
        # 创建弹窗（Toplevel是子窗口）
        popup = tkinter.Toplevel(self.root)
        #popup.overrideredirect(True)  # 同样移除弹窗边框
        popup.attributes('-alpha', 0)  # 初始完全透明（为淡入效果做准备）
        popup.configure(bg=color)     # 设置弹窗背景色
        
        # 随机设置弹窗位置（屏幕坐标）- 使用屏幕宽度和高度确保不会超出屏幕
        x = random.randint(100, self.root.winfo_screenwidth() - 200)
        y = random.randint(100, self.root.winfo_screenheight() - 100)
        popup.geometry(f'200x100+{x}+{y}')  # 宽200像素，高100像素
        
        # 创建标签控件显示祝福语（字体颜色改为黑色）
        label = tkinter.Label(popup, text=blessing, font=('微软雅黑', 12), 
                            bg=color, fg='black', wraplength=180)
        label.pack(expand=True)  # 将标签填充到弹窗中，expand=True使文字居中
        
        return popup

    #执行弹窗显示动画
    def animate_popup(self, popup):
        """只执行淡入效果，窗口不再消失，动画时间缩短到0.1秒"""
        try:
            # 淡入效果：透明度从0%渐增至100%，总共10帧，每帧n秒，总计10n秒
            for i in range(10):
                alpha = i * 0.1
                popup.attributes('-alpha', alpha)
                popup.update()  # 立即更新UI
                time.sleep(0.03)  # 每帧n秒，总计10n秒
            
            # 确保窗口完全可见
            popup.attributes('-alpha', 1.0)
            popup.update()
            
        except Exception as e:
            print(f"动画执行出错: {e}")
            
    def play_background_music(self, music_path=None):
        """
        播放背景音乐，脚本结束后继续播放直到手动中止
        """
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)  # 设置音量为50%
        
        # 如果没有提供音乐文件路径，让用户输入
        if not music_path:
            music_path = input("请输入要播放的音乐文件路径（支持.mp3, .wav等格式），或直接回车跳过音乐播放：")
            if not music_path.strip():
                return  # 用户选择跳过音乐播放
        
        # 处理PyInstaller打包后的路径
        if hasattr(sys, '_MEIPASS'):
            # 如果是打包后的exe，音乐文件在临时目录
            base_path = sys._MEIPASS
            music_file = os.path.join(base_path, os.path.basename(music_path))
        else:
            # 如果是直接运行python脚本，使用当前目录
            music_file = music_path
        
        try:
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play(-1)  # -1表示循环播放
            print("音乐播放中...")
        except pygame.error as e:
            print(f"无法播放音乐: {e}")



# 使用示例
popup_system = BlessingPopup()  # 创建弹窗系统实例

# 播放背景音乐
popup_system.play_background_music(r"浆果.mp3")

print(f"开始生成{len(popup_system.blessings)}个永不消失的祝福窗口...")
print(f"祝福语文本库已包含{len(popup_system.blessings)}条不同的问候语")
nums = len(popup_system.blessings)

# 生成nums个窗口，依次顺序显示，一个完成动画后再显示下一个，无额外间隔
for i in range(nums):
    popup = popup_system.create_popup()
    # 在主线程中直接执行动画，确保顺序执行
    popup_system.animate_popup(popup)
    # 不需要额外的时间间隔，动画完成后立即开始下一个

print(f"{nums}个窗口已全部生成完成！")
print("音乐将持续播放，直到手动关闭程序...")

# 启动主事件循环，保持程序运行
popup_system.root.mainloop()