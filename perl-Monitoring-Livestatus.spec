%define upstream_name    Monitoring-Livestatus
%define upstream_version 0.84

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Monitoring::Livestatus::Class::Abstract::Filter\\)|perl\\(Monitoring::Livestatus::Class::Abstract::Stats\\)'
%endif

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Connector with multiple peers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/sni/Monitoring-Livestatus
Source0:	https://cpan.metacpan.org/authors/id/N/NI/NIERLEIN/Monitoring-Livestatus-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(IO::Socket::INET)
BuildRequires:	perl(IO::Socket::UNIX)
BuildRequires:	perl(JSON::XS)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Thread::Queue)
BuildRequires:	perl(utf8)
BuildArch:	noarch

%description
This module connects via socket/tcp to the check_mk livestatus addon for
Nagios and Icinga. You first have to install and activate the mklivestatus
addon in your monitoring installation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.640.0-2mdv2011.0
+ Revision: 657795
- rebuild for updated spec-helper

* Sat Jan 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.640.0-1mdv2011.0
+ Revision: 627147
- import perl-Monitoring-Livestatus

