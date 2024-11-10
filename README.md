# CLI2Web

CLI2Web 是一个将命令行工具转换为 Web 界面的工具。它能自动解析命令行程序的帮助信息，生成对应的 Web 表单界面，让用户可以通过浏览器来使用命令行工具。

## 特性

- 自动解析命令行程序的帮助信息
- 生成友好的 Web 界面
- 实时显示命令执行输出
- 支持标准输入
- 支持命令行参数的可视化配置
- 响应式设计，支持移动设备

## 实现思路

1. **命令解析**
   - 使用 subprocess 执行命令的 --help 选项获取帮助信息
   - 通过正则表达式解析帮助信息，提取命令选项
   - 自动识别选项类型（标志、值等）

2. **Web 界面**
   - 使用 Flask 作为 Web 框架
   - 使用 Socket.IO 实现实时输出
   - 采用响应式设计，提供良好的移动端体验

3. **命令执行**
   - 使用 subprocess 异步执行命令
   - 通过线程管理命令执行和输出
   - 支持实时输出和错误处理

## 安装部署

### 方法一：从 PyPI 安装（推荐）

```bash
pip install cli2web
```

安装完成后可以直接使用 `cli2web` 命令：
```bash
cli2web <command_name>
```

### 方法二：从源码安装

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/cli2web.git
cd cli2web
```

2. 安装包及其依赖：
```bash
pip install -e .
```

### 方法三：开发环境安装

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/cli2web.git
cd cli2web
```

2. 创建并激活虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. 安装开发依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

### 1. 作为命令行工具使用（安装后）

基本用法：
```bash
cli2web <command_name>
```

完整选项：
```bash
cli2web [-h] [--host HOST] [--port PORT] command

位置参数:
  command            要转换的命令行工具名称

可选参数:
  -h, --help        显示帮助信息
  --host HOST       监听的主机地址 (默认: localhost)
  --port PORT       监听的端口号 (默认: 5000)
```

示例：
```bash
# 使用默认配置
cli2web ls

# 指定端口
cli2web --port 8080 ls

# 指定主机和端口
cli2web --host 0.0.0.0 --port 8080 ls
```

### 2. 作为 Python 模块使用（开发环境）

基本用法：
```bash
python -m cli2web <command_name>
```

完整选项：
```bash
python -m cli2web [-h] [--host HOST] [--port PORT] command
```

示例：
```bash
# 使用默认配置
python -m cli2web ls

# 指定端口
python -m cli2web --port 8080 ls

# 指定主机和端口
python -m cli2web --host 0.0.0.0 --port 8080 ls
```

### 3. 访问 Web 界面

启动服务后，打开浏览器访问显示的地址，例如：
```
http://localhost:5000  # 默认配置
http://localhost:8080  # 自定义端口
```

## 功能特点

1. **自动解析命令选项**
   - 支持短选项和长选项
   - 自动识别必选和可选参数
   - 智能解析选项描述

2. **实时命令执行**
   - WebSocket 实时输出
   - 区分标准输出和错误输出
   - 显示命令执行状态和返回值

3. **用户友好界面**
   - 响应式布局
   - 实时命令行预览
   - 参数可视化配置
   - 支持标准输入

## 技术栈

- **后端**
  - Python 3.8+
  - Flask
  - Flask-SocketIO
  - Eventlet

- **前端**
  - HTML5
  - CSS3
  - JavaScript
  - Socket.IO Client

## 注意事项

1. **安全性**
   - 该工具目前主要用于开发环境
   - 不建议在生产环境中直接使用
   - 注意命令注入风险
   - 建议在受信任的网络环境中使用

2. **兼容性**
   - 支持大多数标准的命令行工具
   - 某些特殊格式的帮助信息可能无法正确解析
   - 建议先测试目标命令的兼容性
   - 确保命令行工具支持 --help 选项

3. **性能**
   - 适合短时间运行的命令
   - 对于长时间运行的命令，建议使用适当的超时设置
   - 注意内存和 CPU 使用情况
   - 避免同时执行过多命令

4. **网络**
   - 默认监听 localhost:5000
   - 可以通过 --host 和 --port 参数配置监听地址和端口
   - 如果需要从其他设备访问，可以设置 --host 0.0.0.0
   - 注意 WebSocket 连接的稳定性
   - 建议在受信任的网络环境中使用

## 开发计划

1. **近期计划**
   - 添加命令历史记录
   - 支持保存常用参数配置
   - 改进命令解析准确性
   - 添加更多的错误处理

2. **长期计划**
   - 支持更多命令行工具
   - 添加用户认证
   - 提供 API 接口
   - 支持命令管道

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 问题反馈

如果您在使用过程中遇到任何问题，或有任何建议，请通过以下方式反馈：

1. 提交 Issue
2. 发送邮件
3. 参与讨论

## 开源协议

MIT License

Copyright (c) 2024 skyfire

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.