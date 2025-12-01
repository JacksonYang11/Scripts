import os
import glob #Python标准库，用于根据文件名模式匹配文件路径，支持通配符 * 、 ? 等

"""
    该脚本用于对指定文件夹下的图片按默认排序后的序号进行批量重命名
    >>>输入：文件夹路径
    >>>执行：找到文件夹下所有类型的图片文件，按默认排序，用排序后的下标号对文件进行批量重命名，比如01.jpg、02.jpg、03.jpg...99.jpg。
    返回：无返回内容
"""


def rename_images(folder_path):
    # 支持的图片扩展名（不区分大小写）
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp")
    
    # 获取文件夹中所有图片文件
    # os.path.join用于拼接路径，这里是构建路径表达式
    # glob.glob()用于根据路径模式查找文件
    files = [f for f in glob.glob(os.path.join(folder_path, "*")) 
             if f.lower().endswith(image_extensions)]
    
    if not files:
        print("未在指定文件夹中找到图片文件。")
        return
    
    # 按操作系统默认顺序（通常是字母顺序）对文件进行排序
    files.sort()
    
    # 计算需要的数字位数填充
    total_files = len(files)
    padding = len(str(total_files))
    
    print(f"找到 {total_files} 个图片文件。")
    print("正在重命名文件...")
    
    # 重命名每个文件
    for index, file_path in enumerate(files, start=1):
        # 获取原始文件扩展名
        # 分割文件路径为文件名和扩展名，返回元组 (name, extension)，[1] 取扩展名部分
        file_extension = os.path.splitext(file_path)[1]
        
        # 生成带填充的新文件名
        # index是要格式化的内容，0{padding}d是指填充padding位整数，填充内容是0
        new_filename = f"{index:0{padding}d}{file_extension}"
        new_file_path = os.path.join(folder_path, new_filename)
        
        # 重命名文件
        os.rename(file_path, new_file_path)
        # os.path.basename() ：获取文件名（不包含路径）
        print(f"✓ 已重命名: {os.path.basename(file_path)} → {new_filename}")
    
    print(f"\n重命名完成！所有图片已从 01 重命名到 {total_files:0{padding}d}。")

if __name__ == "__main__":
    # 让用户输入文件夹路径
    images_folder = input("请输入图片文件夹路径（示例：D:\\Photos\\旅行 或 D:/Photos/旅行）：")
    # 处理路径分隔符，确保Windows兼容性
    images_folder = os.path.normpath(images_folder)
    
    if os.path.exists(images_folder):
        rename_images(images_folder)
    else:
        print(f"错误: 文件夹 '{images_folder}' 不存在。请检查路径是否正确。")