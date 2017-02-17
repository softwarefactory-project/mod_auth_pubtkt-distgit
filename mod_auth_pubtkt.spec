%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_moddir: %{expand: %%global _httpd_moddir %%{_libdir}/httpd/modules}}

Name:           mod_auth_pubtkt
Version:        0.10
Release:        1%{?dist}
Summary:        A pragmatic Web Single Sign-On (SSO) solution

License:        ASL 2.0
URL:            https://neon1.net/mod_auth_pubtkt/
Source0:        https://github.com/manuelkasper/mod_auth_pubtkt/archive/v%{version}.tar.gz

BuildRequires:  openssl-devel
BuildRequires:  httpd-devel
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  binutils
Requires:       httpd


%description
A pragmatic Web Single Sign-On (SSO) solution


%prep
%setup -n %{name}-%{version}


%build
./configure --apxs=/usr/bin/apxs
make
strip src/.libs/mod_auth_pubtkt.so


%install
install -p -D -m 0755 src/.libs/mod_auth_pubtkt.so %{buildroot}%{_httpd_moddir}/mod_auth_pubtkt.so


%files
%{_httpd_moddir}/mod_auth_pubtkt.so


%changelog
* Fri Feb 17 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 0.10-1
- Initial packaging
