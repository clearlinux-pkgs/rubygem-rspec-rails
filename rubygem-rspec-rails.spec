#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rspec-rails
Version  : 3.5.0
Release  : 12
URL      : https://rubygems.org/downloads/rspec-rails-3.5.0.gem
Source0  : https://rubygems.org/downloads/rspec-rails-3.5.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-actionpack
BuildRequires : rubygem-activesupport
BuildRequires : rubygem-ammeter
BuildRequires : rubygem-cucumber
BuildRequires : rubygem-railties
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support

%description
# rspec-rails [![Build Status](https://secure.travis-ci.org/rspec/rspec-rails.svg?branch=master)](http://travis-ci.org/rspec/rspec-rails) [![Code Climate](https://img.shields.io/codeclimate/github/rspec/rspec-rails.svg)](https://codeclimate.com/github/rspec/rspec-rails)
**rspec-rails** is a testing framework for Rails 3.x and 4.x.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rspec-rails-3.5.0
gem spec %{SOURCE0} -l --ruby > rubygem-rspec-rails.gemspec

%build
export LANG=C
gem build rubygem-rspec-rails.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rspec-rails-3.5.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/rspec-rails-3.5.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/.document
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/Capybara.md
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/Changelog.md
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/LICENSE.md
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/controller/controller_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/controller/templates/controller_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/controller/templates/view_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/feature/feature_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/feature/templates/feature_singular_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/feature/templates/feature_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/helper/helper_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/helper/templates/helper_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/install/install_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/install/templates/spec/rails_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/integration/integration_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/integration/templates/request_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/job/job_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/job/templates/job_spec.rb.erb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/mailer/mailer_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/mailer/templates/fixture
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/mailer/templates/mailer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/mailer/templates/preview.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/model/model_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/model/templates/fixtures.yml
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/model/templates/model_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/observer/observer_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/observer/templates/observer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/request/request_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/scaffold/scaffold_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/scaffold/templates/controller_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/scaffold/templates/edit_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/scaffold/templates/index_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/scaffold/templates/new_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/scaffold/templates/routing_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/scaffold/templates/show_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/view/templates/view_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/generators/rspec/view/view_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec-rails.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/active_record.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/adapters.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/configuration.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/example.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/example/controller_example_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/example/feature_example_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/example/helper_example_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/example/job_example_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/example/mailer_example_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/example/model_example_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/example/rails_example_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/example/request_example_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/example/routing_example_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/example/view_example_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/extensions.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/extensions/active_record/proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/feature_check.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/file_fixture_support.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/fixture_support.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/matchers.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/matchers/active_job.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/matchers/be_a_new.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/matchers/be_new_record.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/matchers/be_valid.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/matchers/have_http_status.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/matchers/have_rendered.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/matchers/redirect_to.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/matchers/relation_match_array.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/matchers/routing_matchers.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/tasks/rspec.rake
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/vendor/capybara.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/view_assigns.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/view_path_builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/view_rendering.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-rails-3.5.0/lib/rspec/rails/view_spec_methods.rb
/usr/lib64/ruby/gems/2.3.0/specifications/rspec-rails-3.5.0.gemspec
