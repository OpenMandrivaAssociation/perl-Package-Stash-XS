%define modname	Package-Stash-XS

Summary:	Faster and more correct implementation of the Package::Stash API
Name:		perl-%{modname}
Version:	0.30
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Package::Stash::XS
Source0:	http://www.cpan.org/modules/by-module/Package/Package-Stash-XS-%{version}.tar.gz
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Test::Needs)
BuildRequires:	perl-devel

%description
This is a backend for the Package::Stash manpage, which provides the
functionality in a way that's less buggy and much faster. It will be used
by default if it's installed, and should be preferred in all environments
with a compiler.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%make_install

%files
%doc README Changes LICENSE META.yml META.json
%{perl_vendorarch}/*
%{_mandir}/man3/*
