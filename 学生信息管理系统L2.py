# -*- coding:utf-8 -*-
# @Time    : 2023/6/9 15:14
# @Author  : sunh

"""
作业内容
编写学员实体类，对应属性包含：学号、姓名、性别。
编写学员名单管理类，实现删除学员方法、查询学员方法。
学员实体类添加一个私有属性成绩，要求实现对应的 getter 和 setter。
实现更新学员、添加学员操作。
"""
from typing import List

from dataclasses import dataclass


@dataclass
class Student:
    student_id: int
    name: str
    gender: str

    # 私有属性
    __achievement: int
    
    @property
    def achievement(self):
        return self.__achievement

    @achievement.setter
    def achievement(self, value):
        self.__achievement = value


class StudentList:
    def __init__(self, student_list: List[Student]):
        self.s_list = student_list

    def get(self, student_id: int):
        """
        根据 student_id 查询信息
        """
        for student in self.s_list:
            if student.student_id == student_id:
                return student
            return None

    def delete(self, student_id: int):
        """
        根据 student_id 删除信息
        """
        for student in self.s_list:
            if student.student_id == student_id:
                self.s_list.remove(student)
        # print(self.s_list)

    def update(self, student: Student):
        """
        更新指定学生的信息
        """
        for i, s in enumerate(self.s_list):
            if s.student_id == student.student_id:
                self.s_list[i] = student
                break
        # print(self.s_list)

    def save(self, student: Student):
        for i, s in enumerate(self.s_list):
            if s.student_id == student.student_id:
                print(f"学号为{student.student_id}的学员已存在")
                break
            else:
                self.s_list.append(student)
                break


if __name__ == '__main__':
    # 入参自己定义
    s1 = Student(1, "张三", "男")
    s2 = Student(2, "李四", "女")
    s3 = Student(3, "王五", "男")
    s4 = Student(3, "赵四", "男")
    s5 = Student(4, "七七", "女")

    # print(s1)
    # 初始化一个成员名单
    s_list = StudentList([s1, s2, s3])
    # 实现save
    s_list.save(s5)
    # # 实现update
    # s_list.update(s4)
    # 实现get()方法
    # print(s_list.get(1))
    # # 实现delete
    # s_list.delete(1)
    # 打印操作后的学生列表
    for student in s_list.s_list:
        print(f"学号：{student.student_id}，姓名：{student.name}，性别：{student.gender}")
