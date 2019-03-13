# Nessus_to_report

Nessus扫描完成，总要花挺多时间去整理报告，为此写了一个小脚本，用于自动化生成中文漏洞报告。

解析html报告，自动翻译成中文，并提供修复建议，减少整理报告的时间，提升工作效率。

#### 使用文档

```
Nessus_to_report
 
│ Nessus_report_demo.py       //demo
│ Nessus_report.py           //主文件
│ README.md                 
│ vuln.db                     //中文漏洞库
│
└─img
　　　　01.png
```

1、Nessus扫描结束，选择HTML类型，Report选择Custom，Croup By 选择Host，导出HTML报告。

2、运行脚本：Nessus_resport.py  test.html

在同目录下，生成CSV文件，包含服务器IP、漏洞名称、风险级别、漏洞描述、修复建议。

![](https://raw.githubusercontent.com/Bypass007/Nessus_to_report/master/img/01.png)

#### 参考资料

中文漏洞库：https://github.com/FunnyKun/NessusReportInChinese
