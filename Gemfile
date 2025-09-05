source "https://rubygems.org"
- name: Install dependencies
  run: |
    gem install bundler
    bundle install
    bundle add github-pages

gem "github-pages", group: :jekyll_plugins

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
end

