# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
    config.vm.define "develop" do |develop|
	    develop.vm.box = "ubuntu/xenial64"
	    develop.vm.box_url = "https://vagrantcloud.com/ubuntu/xenial64"
	    develop.vm.box_check_update = "true"

	####Network
		develop.vm.network :forwarded_port, guest: 8000, host: 8000
		develop.vm.network :private_network, ip: '192.168.80.50'
		develop.vm.synced_folder ".", "/vagrant", type: "nfs", mount_options: ['nolock,vers=3,udp,noatime,actimeo=1']
		#develop.vm.synced_folder ".", "/vagrant", type: :virtualbox

    ####Ansible Provision
        develop.vm.provision "ansible_local" do |ansible|
            ansible.compatibility_mode = "2.0"
            ansible.verbose = "vv"
            ansible.playbook = "ansible/vagrant.yml"
        end

	####System Resources
		develop.vm.hostname = "develop"
            develop.vm.provider "virtualbox" do |v|
                v.memory = 2048
                v.cpus = 1
            end
	end
end
