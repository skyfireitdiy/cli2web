import subprocess
import re
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict, Any

@dataclass
class CommandOption:
    name: str
    long_name: Optional[str]
    description: str
    is_required: bool
    has_value: bool = True
    value_type: str = 'text'
    default_value: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'long_name': self.long_name,
            'description': self.description,
            'is_required': self.is_required,
            'has_value': self.has_value,
            'value_type': self.value_type,
            'default_value': self.default_value
        }

class CliParser:
    def __init__(self, command_name: str):
        self.command_name = command_name
        self.options: List[CommandOption] = []
        
    def parse_help(self) -> List[CommandOption]:
        """解析命令行程序的help输出"""
        try:
            help_output = subprocess.check_output(
                [self.command_name, '--help'],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            
            # 使用正则表达式解析help输出
            option_pattern = r'-(\w)(?:,?\s+--([^\s]+))?\s+([^\n]+)'
            matches = re.finditer(option_pattern, help_output)
            
            for match in matches:
                short_name, long_name, description = match.groups()
                # 检查描述中是否包含参数说明（通常在尖括号或方括号中）
                has_value = bool(re.search(r'[<\[].*?[\]>]', description))
                
                self.options.append(
                    CommandOption(
                        name=f'-{short_name}',
                        long_name=f'--{long_name}' if long_name else None,
                        description=description.strip(),
                        is_required='required' in description.lower(),
                        has_value=has_value
                    )
                )
                
            return self.options
            
        except subprocess.CalledProcessError:
            # 如果无法解析help输出，返回基本的标准输入选项
            return [
                CommandOption(
                    name='input',
                    long_name=None,
                    description='Standard input for the command',
                    is_required=False,
                    has_value=True,
                    value_type='textarea'
                )
            ] 