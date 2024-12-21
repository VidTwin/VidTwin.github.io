from PIL import Image, ImageSequence

def compress_gif(input_path, output_path, optimize=True, colors=256):
    # 读取GIF文件
    gif = Image.open(input_path)
    
    # 获取所有帧
    frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]
    
    # 压缩每一帧
    compressed_frames = []
    for frame in frames:
        frame = frame.convert("P", palette=Image.ADAPTIVE, colors=colors)
        compressed_frames.append(frame)
    
    # 获取duration和loop信息，如果不存在则设置默认值
    duration = gif.info.get('duration', 100)  # 默认值为100毫秒
    loop = gif.info.get('loop', 0)  # 默认值为0（无限循环）

    # 保存压缩后的GIF
    compressed_frames[0].save(
        output_path,
        save_all=True,
        append_images=compressed_frames[1:],
        optimize=optimize,
        duration=duration,
        loop=loop
    )

def main():
    input_path = 'video/cross/1.gif'  # 输入GIF文件路径
    output_path = 'video/cross/1_compress.gif'  # 输出压缩后的GIF文件路径
    
    compress_gif(input_path, output_path)

if __name__ == "__main__":
    main()