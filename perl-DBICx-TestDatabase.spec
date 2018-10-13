#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DBICx-TestDatabase
Version  : 0.05
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/J/JR/JROCKWAY/DBICx-TestDatabase-0.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JR/JROCKWAY/DBICx-TestDatabase-0.05.tar.gz
Summary  : 'create a temporary database from a DBIx::Class::Schema'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(DBD::SQLite)
BuildRequires : perl(DBIx::Class)
BuildRequires : perl(Module::Install)
BuildRequires : perl(SQL::Translator)

%description
This is a CPAN module:
perl Makefile.PL
make
make test
sudo make install
See "perldoc DBICx::TestDatabase" for more info.

%package dev
Summary: dev components for the perl-DBICx-TestDatabase package.
Group: Development
Provides: perl-DBICx-TestDatabase-devel = %{version}-%{release}

%description dev
dev components for the perl-DBICx-TestDatabase package.


%prep
%setup -q -n DBICx-TestDatabase-0.05

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/DBICx/TestDatabase.pm
/usr/lib/perl5/vendor_perl/5.26.1/DBICx/TestDatabase/Subclass.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DBICx::TestDatabase.3
/usr/share/man/man3/DBICx::TestDatabase::Subclass.3
