Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.define :tbl do |web_config|
    config.vm.network "forwarded_port", guest: 80, host: 80
    config.vm.provision "shell", path: "scripts/bootstrap.sh"
  end
end
