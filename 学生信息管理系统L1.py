# -*- coding:utf-8 -*-
# @Time    : 2023/6/6 21:00
# @Author  : sunh

# 作业内容
# 编写学员实体类，对应属性包含：学号、姓名、性别。
# 编写学员名单管理类，实现删除学员方法、查询学员方法.


class Student:
    """
    自己根据题目要求实现
    """
    def __init__(self, student_id, name, gender):
        self.student_id = student_id
        self.name = name
        self.gender = gender


class StudentList:
    def __init__(self, student_list):
        self.s_list = student_list

    def get(self, student_id):
        """
        根据 student_id 查询信息
        """
        for student in self.s_list:
            if student.student_id == student_id:
                return student
        return None

    def delete(self, student_id):
        """
        根据 student_id 删除信息
        """
        for student in self.s_list:
            if student.student_id == student_id:
                self.s_list.remove(student)
                return True
        return False


if __name__ == '__main__':
    # 入参自己定义
    s1 = Student("1","张三","男")
    s2 = Student("2","李四","女")
    s3 = Student("3","王五","男")
    # 初始化一个成员名单
    s_list = StudentList([s1, s2, s3])
    # 实现get()方法
    print(s_list.get("2").name)
    # 实现delete
    print(s_list.delete("2"))