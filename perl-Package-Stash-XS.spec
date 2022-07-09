%define modname	Package-Stash-XS
%define modver 0.30

Summary:	Faster and more correct implementation of the Package::Stash API
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Package::Stash::XS
Source0:	http://www.cpan.org/modules/by-module/Package/Package-Stash-XS-%{modver}.tar.gz
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl-devel

%description
This is a backend for the Package::Stash manpage, which provides the
functionality in a way that's less buggy and much faster. It will be used
by default if it's installed, and should be preferred in all environments
with a compiler.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{perl_vendorarch}/*
%{_mandir}/man3/*
