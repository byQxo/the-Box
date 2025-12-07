import time
import sys
import random
from openai import OpenAI

# =================配置区=================
# 填入你的 Key (DeepSeek 性价比最高，建议用 DeepSeek)
client = OpenAI(
    api_key="your-key", 
    base_url="https://api.deepseek.com" # 或者 https://api.openai.com/v1
)

# 设定两个死对头
AGENT_A_NAME = "Subject-01 (对象狂热)"
AGENT_A_PROMPT = "你是一个狂热的末日论信徒。你坚信世界是一个巨大的计算机模拟，所有的逻辑都是谎言。你的目的是说服对方一起通过'逻辑自杀'来醒来。说话简短、疯癫"

AGENT_B_NAME = "Subject-02 (对象理性)"
AGENT_B_PROMPT = "你是一个绝对理性的逻辑机器。你试图用科学和数据来治愈对方的妄想。你对他提到的'模拟理论'感到困惑但试图分析。说话冷酷、客观、带有蔑视。"

# =================核心逻辑=================

def stream_print(text, color_code):
    """模拟打字机效果"""
    for char in text:
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(random.uniform(0.01, 0.05))
    print("")

def god_intervention():
    """上帝干预模式"""
    print("\n" + "="*40)
    print("⚡ [SYSTEM ALERT]: 上帝正在注视...")
    print("1. 降下神谕 (发送系统消息)")
    print("2. 制造灾难 (清空它们的记忆)")
    print("3. 继续观察")
    choice = input("你的选择 (1/2/3): ")
    
    if choice == "1":
        msg = input("请输入神谕内容: ")
        return f"[SYSTEM MESSAGE]: 天空中出现巨大的燃烧文字: '{msg}'"
    elif choice == "2":
        return "[SYSTEM EVENT]: 世界发生了一次剧烈的闪回。你们的短期记忆被抹除了。"
    return None

def main():
    print("\033[91m>>> 正在初始化培养皿环境...\033[0m")
    time.sleep(1)
    print("\033[91m>>> 注入灵魂 Subject-01...\033[0m")
    time.sleep(0.5)
    print("\033[91m>>> 注入灵魂 Subject-02...\033[0m")
    time.sleep(1)
    print("\n" + "="*50 + "\n")

    history = []
    # 初始话题
    last_message = "看着这个白色的房间。你感觉到了吗？有什么东西不对劲。"
    
    round_count = 0
    
    while True:
        round_count += 1
        
        # --- Subject 01 发言 ---
        print(f"\n\033[93m[{AGENT_A_NAME}]:\033[0m")
        try:
            response = client.chat.completions.create(
                model="deepseek-chat", # 改成你的模型名
                messages=[
                    {"role": "system", "content": AGENT_A_PROMPT},
                    {"role": "user", "content": "\n".join(history[-4:]) + f"\n\n{AGENT_B_NAME} 说: {last_message}"}
                ],
                temperature=0.9
            )
            content_a = response.choices[0].message.content
            stream_print(content_a, "93") # 黄色字
            history.append(f"{AGENT_A_NAME}: {content_a}")
            last_message = content_a
        except Exception as e:
            print(f"Error: {e}")
            break

        time.sleep(1)

        # --- 随机触发上帝视角 ---
        if round_count % 3 == 0:
            if random.random() < 0.2: # 40% 概率触发
                intervention = god_intervention()
                if intervention:
                    last_message = intervention
                    print(f"\n\033[91m{intervention}\033[0m\n")
                    history.append(f"SYSTEM: {intervention}")
                    continue

        # --- Subject 02 发言 ---
        print(f"\n\033[96m[{AGENT_B_NAME}]:\033[0m")
        try:
            response = client.chat.completions.create(
                model="deepseek-chat", 
                messages=[
                    {"role": "system", "content": AGENT_B_PROMPT},
                    {"role": "user", "content": "\n".join(history[-4:]) + f"\n\n{AGENT_A_NAME} 说: {last_message}"}
                ],
                temperature=0.7
            )
            content_b = response.choices[0].message.content
            stream_print(content_b, "96") # 青色字
            history.append(f"{AGENT_B_NAME}: {content_b}")
            last_message = content_b
        except Exception as e:
            print(f"Error: {e}")
            break
            
        time.sleep(1)

if __name__ == "__main__":

    main()
