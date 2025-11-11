import tkinter  # 导入Tkinter主模块
import random   # 用于随机选择祝福语和颜色
import time     # 控制动画时间间隔

class BlessingPopup:
    def __init__(self):
        # 创建主窗口（但不显示），作为弹窗的寄生容器
        self.root = tkinter.Tk()
        self.root.overrideredirect(True)   # 移除窗口边框和标题栏
        self.root.attributes('-alpha', 0)   # 设置主窗口完全透明，避免显示
        self.root.attributes('-topmost', True) # 窗口始终置顶
        
        # 数据源：祝福语列表（增加到60条）和颜色列表
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
            "保持善良", "多和朋友联系", "享受阳光", "保持一颗年轻的心",
            "小确幸也很重要", "学会放下", "拥抱变化", "你的存在很有意义",
            "记得要开心", "简单生活，热爱所爱", "平凡中的美好", "每一步都算数",
            "生活需要仪式感", "保持积极心态", "笑一笑，十年少", "你很棒，别怀疑"
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
            # 淡入效果：透明度从0%渐增至100%，总共10帧，每帧0.01秒，总计0.1秒
            for i in range(10):
                alpha = i * 0.1
                popup.attributes('-alpha', alpha)
                popup.update()  # 立即更新UI
                time.sleep(0.01)  # 每帧0.01秒，10帧总共0.1秒
            
            # 确保窗口完全可见
            popup.attributes('-alpha', 1.0)
            popup.update()
            
        except Exception as e:
            print(f"动画执行出错: {e}")



# 使用示例
popup_system = BlessingPopup()  # 创建弹窗系统实例
print("开始生成20个永不消失的祝福窗口...")
print(f"祝福语文本库已包含{len(popup_system.blessings)}条不同的问候语")
nums = len(popup_system.blessings)

# 生成nums个窗口，依次顺序显示，一个完成动画后再显示下一个，无额外间隔
for i in range(nums):
    popup = popup_system.create_popup()
    # 在主线程中直接执行动画，确保顺序执行
    popup_system.animate_popup(popup)
    # 不需要额外的时间间隔，动画完成后立即开始下一个

print(f"{nums}个窗口已全部生成完成！")
print("窗口中字体颜色已更改为黑色，以提高可读性")

# 启动主事件循环，保持程序运行
popup_system.root.mainloop()