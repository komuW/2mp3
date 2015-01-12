#!/usr/bin/env ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "precise32"

  # The url from where the 'config.vm.box' box will be fetched.
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  # Create a forwarded port mapping which allows access to a specific port 
  config.vm.network :forwarded_port, guest: 4500, host: 4500,

  config.ssh.forward_agent = true
  
  # Bootstrap provisioning with the shell.
  config.vm.provision :shell, :path => "boot.sh"

  # Cache apt-get package downloads to speed things up
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
  end

end
