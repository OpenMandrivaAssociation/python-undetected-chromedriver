Name:		python-undetected-chromedriver
Version:	3.5.5
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/u/undetected-chromedriver/undetected-chromedriver-%{version}.tar.gz
Summary:	Selenium.webdriver.Chrome replacement
URL:		https://pypi.org/project/undetected-chromedriver/
License:	GPL-3.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Selenium.webdriver.Chrome replacement with compatiblity for Brave,
and other Chromium based browsers.

Not triggered by CloudFlare/Imperva/hCaptcha and such.

NOTE: results may vary due to many factors. No guarantees are given, except
for ongoing efforts in understanding detection algorithms.

%files
%{py_sitedir}/undetected_chromedriver
%{py_sitedir}/undetected_chromedriver-*.*-info
