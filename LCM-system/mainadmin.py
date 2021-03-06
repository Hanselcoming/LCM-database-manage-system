# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from service import service
from M_query import basicinfo, physicshape, sph, acid, fric, compress, abrasion, temper
from M_manage import basicinfo2, physicshape2, sph2, acid2, fric2, compress2, abrasion2, temper2
import sys
import qdarkstyle

from user_manage import user, admin


class Ui_MainWindow(QMainWindow):
    # 构造方法
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)  # 只显示最小化和关闭按钮
        self.setupUi(self)  # 初始化窗体设置

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(899, 556)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/T1/images/swpu.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border-image:url(:/T1/images/main.jpg)")
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 34))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_7 = QtWidgets.QMenu(self.menu)
        self.menu_7.setObjectName("menu_7")
        self.menu_5 = QtWidgets.QMenu(self.menu)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menu)
        self.menu_6.setObjectName("menu_6")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionbasicinfo = QtWidgets.QAction(MainWindow)
        self.actionbasicinfo.setObjectName("actionbasicinfo")
        self.actionphysicshape = QtWidgets.QAction(MainWindow)
        self.actionphysicshape.setObjectName("actionphysicshape")
        self.actionsph = QtWidgets.QAction(MainWindow)
        self.actionsph.setObjectName("actionsph")
        self.actionacid = QtWidgets.QAction(MainWindow)
        self.actionacid.setObjectName("actionacid")
        self.actionfric = QtWidgets.QAction(MainWindow)
        self.actionfric.setObjectName("actionfric")
        self.actioncompress = QtWidgets.QAction(MainWindow)
        self.actioncompress.setObjectName("actioncompress")
        self.actionabrasion = QtWidgets.QAction(MainWindow)
        self.actionabrasion.setObjectName("actionabrasion")
        self.actiontemper = QtWidgets.QAction(MainWindow)
        self.actiontemper.setObjectName("actiontemper")
        self.actionbasicinfo_2 = QtWidgets.QAction(MainWindow)
        self.actionbasicinfo_2.setObjectName("actionbasicinfo_2")
        self.actionphysicshape_2 = QtWidgets.QAction(MainWindow)
        self.actionphysicshape_2.setObjectName("actionphysicshape_2")
        self.actionsph_2 = QtWidgets.QAction(MainWindow)
        self.actionsph_2.setObjectName("actionsph_2")
        self.actionacid_2 = QtWidgets.QAction(MainWindow)
        self.actionacid_2.setObjectName("actionacid_2")
        self.actionfric_2 = QtWidgets.QAction(MainWindow)
        self.actionfric_2.setObjectName("actionfric_2")
        self.actioncompress_2 = QtWidgets.QAction(MainWindow)
        self.actioncompress_2.setObjectName("actioncompress_2")
        self.actionabrasion_2 = QtWidgets.QAction(MainWindow)
        self.actionabrasion_2.setObjectName("actionabrasion_2")
        self.actiontemper_2 = QtWidgets.QAction(MainWindow)
        self.actiontemper_2.setObjectName("actiontemper_2")
        self.actionuserinfo = QtWidgets.QAction(MainWindow)
        self.actionuserinfo.setObjectName("actionuserinfo")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionphysicshape_3 = QtWidgets.QAction(MainWindow)
        self.actionphysicshape_3.setObjectName("actionphysicshape_3")
        self.actionsph_3 = QtWidgets.QAction(MainWindow)
        self.actionsph_3.setObjectName("actionsph_3")
        self.actionacid_3 = QtWidgets.QAction(MainWindow)
        self.actionacid_3.setObjectName("actionacid_3")
        self.actionfric_3 = QtWidgets.QAction(MainWindow)
        self.actionfric_3.setObjectName("actionfric_3")
        self.actioncompress_3 = QtWidgets.QAction(MainWindow)
        self.actioncompress_3.setObjectName("actioncompress_3")
        self.actionabrasion_3 = QtWidgets.QAction(MainWindow)
        self.actionabrasion_3.setObjectName("actionabrasion_3")
        self.actiontemper_3 = QtWidgets.QAction(MainWindow)
        self.actiontemper_3.setObjectName("actiontemper_3")
        self.actionadmin = QtWidgets.QAction(MainWindow)
        self.actionadmin.setObjectName("actionadmin")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/T1/images/appstu.ICO"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionadmin.setIcon(icon2)
        self.actiondesign_jq = QtWidgets.QAction(MainWindow)
        self.actiondesign_jq.setObjectName("actiondesign_jq")
        self.actiondesign_lj = QtWidgets.QAction(MainWindow)
        self.actiondesign_lj.setObjectName("actiondesign_lj")
        self.actiondesign_tc = QtWidgets.QAction(MainWindow)
        self.actiondesign_tc.setObjectName("actiondesign_tc")
        self.menu_7.addAction(self.actionfric_3)
        self.menu_7.addAction(self.actioncompress_3)
        self.menu_7.addAction(self.actionabrasion_3)
        self.menu_5.addAction(self.actionphysicshape_3)
        self.menu_5.addAction(self.actionsph_3)
        self.menu_6.addAction(self.actionacid_3)
        self.menu_6.addAction(self.actiontemper_3)
        self.menu.addAction(self.actionbasicinfo)
        self.menu.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.menu_7.menuAction())
        self.menu.addAction(self.menu_6.menuAction())
        self.menu_2.addAction(self.actionbasicinfo_2)
        self.menu_2.addAction(self.actionphysicshape_2)
        self.menu_2.addAction(self.actionsph_2)
        self.menu_2.addAction(self.actionacid_2)
        self.menu_2.addAction(self.actionfric_2)
        self.menu_2.addAction(self.actioncompress_2)
        self.menu_2.addAction(self.actionabrasion_2)
        self.menu_2.addAction(self.actiontemper_2)
        self.menu_3.addAction(self.actiondesign_jq)
        self.menu_3.addAction(self.actiondesign_lj)
        self.menu_3.addAction(self.actiondesign_tc)
        self.menu_4.addAction(self.actionuserinfo)
        self.menu_4.addAction(self.actionadmin)
        self.menu_4.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        datetime = QtCore.QDateTime.currentDateTime()  # 获取当前日期时间
        self.actionexit.triggered.connect(MainWindow.close)
        time = datetime.toString("yyyy-MM-dd HH:mm:ss")  # 对日期时间进行格式化
        # 状态栏中显示登录用户、登录时间，以及版权信息
        self.statusbar.showMessage("当前登录用户：" + service.userName + " | 登录时间：" + time + "  | 开发制作：西南石油大学", 0)
        # 为材料查询菜单中的QAction绑定triggered信号
        self.menu.triggered[QtWidgets.QAction].connect(self.openQuery)
        # 为材料管理菜单中的QAction绑定triggered信号
        self.menu_2.triggered[QtWidgets.QAction].connect(self.openManage)
        #     # 为系统查询菜单中的QAction绑定triggered信号
        #     self.menu_3.triggered[QtWidgets.QAction].connect(self.openQuery)
        # 为用户管理菜单中的QAction绑定triggered信号
        self.menu_4.triggered[QtWidgets.QAction].connect(self.openUser)

    #
    # 材料查询菜单对应槽函数
    #
    def openQuery(self, m):
        if m.text() == "按基本信息":
            self.m = basicinfo.Ui_MainWindow()  # 创建按基本信息查询窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == '按物理形状':
            self.m = physicshape.Ui_MainWindow()  # 创建班级设置窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == '按圆球度':
            self.m = sph.Ui_MainWindow()  # 创建班级设置窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == '按酸溶率':
            self.m = acid.Ui_MainWindow()  # 创建班级设置窗体对象
            self.m.show()  # 显示窗
        elif m.text() == "按抗高温能力":
            self.m = temper.Ui_MainWindow()  # 创建班级设置窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == '按摩擦系数':
            self.m = fric.Ui_MainWindow()  # 创建班级设置窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == "按抗压能力":
            self.m = compress.Ui_MainWindow()  # 创建班级设置窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == "按抗磨蚀能力":
            self.m = abrasion.Ui_MainWindow()  # 创建班级设置窗体对象
            self.m.show()  # 显示窗体

    # 材料管理菜单对应槽函数
    #
    def openManage(self, m):
        if m.text() == "管理基本信息":
            self.m = basicinfo2.Ui_MainWindow()  # 创建材料管理窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == "管理物理形状":
            self.m = physicshape2.Ui_MainWindow()  # 创建材料管理窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == "管理圆球度":
            self.m = sph2.Ui_MainWindow()  # 创建材料管理窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == "管理酸溶率":
            self.m = acid2.Ui_MainWindow()  # 创建材料管理窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == "管理摩擦系数":
            self.m = fric2.Ui_MainWindow()  # 创建材料管理窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == "管理抗压能力":
            self.m = compress2.Ui_MainWindow()  # 创建材料管理窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == "管理抗磨蚀能力":
            self.m = abrasion2.Ui_MainWindow()  # 创建材料管理窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == "管理抗高温老化性质":
            self.m = temper2.Ui_MainWindow()  # 创建材料管理窗体对象
            self.m.show()  # 显示窗体

    #     # 系统查询菜单对应槽函数
    #
    # def openQuery(self, m):
    #     if m.text() == "学生信息查询":
    #         self.m = studentinfo.Ui_MainWindow()  # 创建学生信息查询窗体对象
    #         self.m.show()  # 显示窗体
    #
    #     # 系统管理菜单对应槽函数
    #
    def openUser(self, m):
        if m.text() == "用户信息":
            self.m = user.Ui_MainWindow()  # 创建用户维护窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == "管理员信息":
            self.m = admin.Ui_MainWindow()  # 创建用户维护窗体对象
            self.m.show()  # 显示窗体

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "防漏堵漏材料数据库管理系统(管理员)"))
        self.menu.setTitle(_translate("MainWindow", "材料查询"))
        self.menu_7.setTitle(_translate("MainWindow", "按力学性质"))
        self.menu_5.setTitle(_translate("MainWindow", "按几何性质"))
        self.menu_6.setTitle(_translate("MainWindow", "按化学性质"))
        self.menu_2.setTitle(_translate("MainWindow", "材料管理"))
        self.menu_3.setTitle(_translate("MainWindow", "配方选材设计"))
        self.menu_4.setTitle(_translate("MainWindow", "用户信息管理"))
        self.actionbasicinfo.setText(_translate("MainWindow", "按基本信息"))
        self.actionphysicshape.setText(_translate("MainWindow", "按物理形状"))
        self.actionsph.setText(_translate("MainWindow", "按圆球度"))
        self.actionsph.setIconText(_translate("MainWindow", "按圆球度"))
        self.actionacid.setText(_translate("MainWindow", "按酸溶率"))
        self.actionfric.setText(_translate("MainWindow", "按摩擦系数"))
        self.actioncompress.setText(_translate("MainWindow", "按抗压能力"))
        self.actionabrasion.setText(_translate("MainWindow", "按磨蚀能力"))
        self.actiontemper.setText(_translate("MainWindow", "按抗高温能力"))
        self.actionbasicinfo_2.setText(_translate("MainWindow", "管理基本信息"))
        self.actionphysicshape_2.setText(_translate("MainWindow", "管理物理形状"))
        self.actionsph_2.setText(_translate("MainWindow", "管理圆球度"))
        self.actionacid_2.setText(_translate("MainWindow", "管理酸溶率"))
        self.actionfric_2.setText(_translate("MainWindow", "管理摩擦系数"))
        self.actioncompress_2.setText(_translate("MainWindow", "管理抗压能力"))
        self.actionabrasion_2.setText(_translate("MainWindow", "管理抗磨蚀能力"))
        self.actiontemper_2.setText(_translate("MainWindow", "管理抗高温老化性质"))
        self.actionuserinfo.setText(_translate("MainWindow", "用户信息"))
        self.actionexit.setText(_translate("MainWindow", "退出系统"))
        self.actionphysicshape_3.setText(_translate("MainWindow", "按物理形状"))
        self.actionsph_3.setText(_translate("MainWindow", "按圆球度"))
        self.actionacid_3.setText(_translate("MainWindow", "按酸溶率"))
        self.actionfric_3.setText(_translate("MainWindow", "按摩擦系数"))
        self.actionfric_3.setToolTip(_translate("MainWindow", "按摩擦系数"))
        self.actioncompress_3.setText(_translate("MainWindow", "按抗压能力"))
        self.actionabrasion_3.setText(_translate("MainWindow", "按抗磨蚀能力"))
        self.actiontemper_3.setText(_translate("MainWindow", "按抗高温能力"))
        self.actionadmin.setText(_translate("MainWindow", "管理员信息"))
        self.actiondesign_jq.setText(_translate("MainWindow", "架桥"))
        self.actiondesign_lj.setText(_translate("MainWindow", "拉筋"))
        self.actiondesign_tc.setText(_translate("MainWindow", "填充"))


import imagess

