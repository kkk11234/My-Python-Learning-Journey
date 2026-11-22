"""学生成绩统计程序

功能：
1. 逐个输入学生成绩（0-100 分），输入 q 结束录入；
2. 自动检查输入是否合法，非数字或超出 0-100 会提示重新输入；
3. 统计人数、总分、平均分、最高分、最低分和及格率；
4. 按 A/B/C/D/F 五个等级统计人数，并用简单的文本柱状图显示分布。

作者：卡米力江（2023341042）
运行方式：python score_statistics.py
"""


def grade_of(score):
    """把百分制分数转换成等级。"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"



