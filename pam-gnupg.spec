%define date 20190205

Summary:	Unlock GnuPG keys on login
Name:		pam-gnupg
Version:	0
Release:	0.%{date}.1
License:	MIT
Group:		System/Libraries
URL:		https://github.com/cruegge/pam-gnupg
#git archive --format=tar --prefix=pam-gnupg-0-$(date +%Y%m%d)/ HEAD | xz -vf > pam-gnupg-0-$(date +%Y%m%d).tar.xz
Source0:	https://github.com/cruegge/pam-gnupg/release/archive/%{name}-%{version}-%{date}.tar.xz
BuildRequires:	pam-devel
Requires:	pam
Requires:	gnupg

%description
A PAM module that hands over your login password 
to gpg-preset-passphrase. This can be e.g. useful 
if you are using a GnuPG-based password manager.

How to include the module in PAM's config depends
on your distribution. You generally have to add the
lines:

auth     optional  pam_gnupg.so
session  optional  pam_gnupg.so

%prep
%autosetup -n %{name}-%{version}-%{date} -p1

%build
./autogen.sh

%configure
%make_build --with-moduledir=/%{_lib}/security

%install
%make_install

%files
%doc README.md
/%{_lib}/security/pam-gnupg.so
