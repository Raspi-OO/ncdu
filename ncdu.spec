Name:           ncdu
Version:        1.15.1
Release:        1
Summary:        Text-based disk usage viewer

License:        MIT
URL:            http://dev.yorhel.nl/ncdu/
Source0:        https://dev.yorhel.nl/download/ncdu-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  ncurses-devel

%description
ncdu (NCurses Disk Usage) is a curses-based version of the well-known 'du',
and provides a fast way to see what directories are using your disk space.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_mandir}/man1/ncdu.1*
%doc ChangeLog
%license COPYING
%{_bindir}/ncdu

%changelog
* Fri Sep 25 2020 Luke Yue <lukedyue@gmail.com> - 1.15.1-1
- Initial package
