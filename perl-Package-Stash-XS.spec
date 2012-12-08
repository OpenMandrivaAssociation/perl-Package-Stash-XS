%define upstream_name    Package-Stash-XS
%define upstream_version 0.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Faster and more correct implementation of the Package::Stash API
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Package/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a backend for the Package::Stash manpage, which provides the
functionality in a way that's less buggy and much faster. It will be used
by default if it's installed, and should be preferred in all environments
with a compiler.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-4mdv2012.0
+ Revision: 765581
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-3
+ Revision: 764092
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-2
+ Revision: 667286
- mass rebuild

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.220.0-1
+ Revision: 643416
- update to new version 0.22

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.210.0-2
+ Revision: 640776
- rebuild to obsolete old packages

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.210.0-1
+ Revision: 635207
- update to new version 0.21

* Wed Jan 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.200.0-1
+ Revision: 633014
- import perl-Package-Stash-XS

