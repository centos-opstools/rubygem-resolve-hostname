# Generated from resolve-hostname-0.0.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name resolve-hostname

Name: rubygem-%{gem_name}
Version: 0.1.0
Release: 1%{?dist}
Summary: Hostname resolver with caching
Group: Development/Languages
License: MIT
URL: https://github.com/tagomoris/resolve-hostname
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
With caching, selector for IPv4/IPv6, and many other features.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/resolve-hostname.gemspec
%{gem_instdir}/spec

%changelog
* Thu Jun 29 2017 Rich Megginson <rmeggins@redhat.com> - 0.1.0-1
- version 0.1.0

* Wed Aug 24 2016 Rich Megginson <rmeggins@redhat.com> - 0.0.4-2
- added Provides for rubygem(resolve-hostname)

* Wed Aug 17 2016 Yanis Guenane <yguenane@redhat.com> - 0.0.4-1
- Initial package
