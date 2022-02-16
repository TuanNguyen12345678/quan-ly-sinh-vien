/*CREATE TABLE DMKHOA
(
Makhoa CHAR(2) PRIMARY KEY,
TenKhoa NVARCHAR(30) NOT NULL
)
SELECT * FROM dbo.DMKHOA


CREATE TABLE DMSV
(
MaSV CHAR(3) NOT NULL PRIMARY KEY,
HoSV NVARCHAR(15) NOT NULL,
TenSV NVARCHAR(7) NOT NULL,
Phai NCHAR(7),
NgaySinh DATETIME NOT NULL,
NoiSinh NVARCHAR(20),
MaKhoa CHAR(2),
HocBong FLOAT
)
SELECT * FROM dbo.DMSV

CREATE TABLE DMMH
(
MaMH CHAR(2) NOT NULL PRIMARY KEY,
TenMH NVARCHAR(25) NOT NULL,
SoTiet TINYINT
)

create table KETQUA 
(
	MaSV char(3) not null, 
	MaMH char(2) not null, 
	LanThi tinyint, 
	Diem decimal(4,2),
	constraint KETQUA_MaSV_MaMH_LanThi_pk primary key (MaSV,MaMH,LanThi)
)
SELECT * FROM KETQUA
/*05 TẠO RÀNG BUỘC KHÓA NGOẠI GIỮA CÁC BẢNG*/
alter table DMSV 
add constraint DMKHOA_MAKHOA_fk foreign key (MaKhoa) references DMKHOA (MaKhoa)
Alter table KETQUA 
add constraint KETQUA_MASV_fk foreign key (MaSV) references DMSV(MaSV), 
constraint DMMH_MAMH_fk foreign key (MaMH) references DMMH(MaMH)
NHẬP DỮ LIỆU VÀO BẢNG DANH MỤC MÔN HỌC N CÓ NGHĨA LÀ UNICODE*/
SELECT * FROM DMMH
INSERT INTO DMMH VALUES ('01',N'Cơ sở dữ liệu',45)
INSERT INTO DMMH VALUES ('02',N'Trí tuệ nhân tạo',45)
INSERT INTO DMMH VALUES ('03',N'Truyền tin',45)
INSERT INTO DMMH VALUES ('04',N'Đồ họa máy tính',60)
INSERT INTO DMMH VALUES ('05',N'Văn phạm',60)
/*NHẬP DỮ LIỆU VÀO BẢNG KHOA */
SELECT * FROM DMKHOA
INSERT INTO DMKHOA VALUES ('AV',N'Anh văn')
INSERT INTO DMKHOA VALUES ('TH',N'Tin học')
INSERT INTO DMKHOA VALUES ('TR',N'Triết')
INSERT INTO DMKHOA VALUES ('VL',N'Vật lý')
/*nhập dữ liệu cho bảng danh mục sinh viên*/
SELECT * FROM DMSV
INSERT INTO DMSV VALUES ('A01',N'Nguyễn Thị',N'Hải',N'Nữ','02/23/1990',N'Hà Nội','TH',130000)
INSERT INTO DMSV VALUES ('A02',N'Trần Văn',N'Chính',N'Nam','12/24/1992',N'Bình Định','VL',150000)
INSERT INTO DMSV VALUES ('A03',N'Lê Thu',N'Bạch',N'Nữ','02/21/1990',N'TP HCM','TH',170000)
SELECT * FROM dbo.KETQUA
INSERT INTO KETQUA VALUES ('A01','01',1,3)
INSERT INTO KETQUA VALUES ('A01','01',2,6)
INSERT INTO KETQUA VALUES ('A02','01',1,7)