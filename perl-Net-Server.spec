%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Net-Server
Summary:	Net::Server perl module
Summary:	Net::Server perl module 
Summary(cs):	Modul Net::Server pro Perl
Summary(da):	Perlmodul Net::Server
Summary(de):	Net::Server Perl Modul
Summary(es):	M�dulo de Perl Net::Server
Summary(fr):	Module Perl Net::Server
Summary(it):	Modulo di Perl Net::Server
Summary(ja):	Net::Server Perl �⥸�塼��
Summary(ko):	Net::Server �� ����
Summary(no):	Perlmodul Net::Server
Summary(pl):	Modu� perla Net::Server
Summary(pt_BR):	M�dulo Perl Net::Server
Summary(pt):	M�dulo de Perl Net::Server
Summary(ru):	������ ��� Perl Net::Server
Summary(sv):	Net::Server Perlmodul
Summary(uk):	������ ��� Perl Net::Server
Summary(zh_CN):	Net::Server Perl ģ��
Name:		perl-Net-Server
Version:	0.84
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"Net::Server" is an extensible, generic Perl server engine.  "Net::Server"
combines the good properties from "Net::Daemon" (0.34), "NetServer::Generic"
(1.03), and "Net::FTPServer" (1.0), and also from various concepts in the
Apache Webserver.

"Net::Server" attempts to be a generic server as in "Net::Daemon" and
"NetServer::Generic". It includes with it the ability to run as an inetd
process ("Net::Server::INET"), a single connection server ("Net::Server" or
"Net::Server::Single"), a forking server ("Net::Server::Fork"), a preforking
server which maintains a constant number of preforked children
("Net::Server::PreForkSimple"), or as a managed preforking server which
maintains the number of children based on server load ("Net::Server::PreFork").
In all but the inetd type, the server provides the ability to connect to one or
to multiple server ports.

%prep
%setup -q -n %{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README examples
%{perl_sitelib}/Net/Server*
%{_mandir}/man3/*
