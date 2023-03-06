# 打开文件并读取所有行内容
with open('xxx.yaml', 'r') as f:
    lines = f.readlines()

# 查找并替换指定字符串
for i in range(len(lines)):
    if 'DOMAIN-SUFFIX,linkedin.com' in lines[i]:
        lines[i] = "    - 'DOMAIN-SUFFIX,linkedin.com,proxy'\n"

# 判断是否需要在文件末尾添加内容
if 'DOMAIN-SUFFIX,openai.com,proxy' not in ''.join(lines):
    lines.append("    - 'DOMAIN-SUFFIX,openai.com,proxy'\n")

# 将修改后的内容写回文件
with open('xxx.yaml', 'w') as f:
    f.writelines(lines)