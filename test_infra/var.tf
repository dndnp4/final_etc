
#######################
# Common
#######################
variable "region" {
  type = string
  default = "ap-northeast-2"
}

variable "az" {
  type = list(string)
  default = ["a", "c"]
}

variable "name_prefix" {
  type = string
  default = "depts"
}

variable "common_ssh_key" {
  type = object({ name = string, path = string })
  default = {
    name = "depts_key"
    path = "./JSkey.pub"
  }
}

#######################
# Networks (CIDR range) 
#######################
variable "cidr_all" {
  type = string
  default = "0.0.0.0/0"
}

variable "cidr_vpc" {
  type = string
  default = "192.168.0.0/16"
}

variable "cidr_public_subnets" {
  type = list(string)
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "cidr_private_subnets" {
  type = list(string)
}

variable "cidr_private_db_subnets" {
  type = list(string)
}

#######################
# EC2
#######################
variable "ec2_webserver_options" {
  type = object(
    {
      ami               = string,
      instance_type     = string,
      user_data_path    = string,
      sample_private_ip = string
    }
  )
}

#######################
# RDS
#######################

variable "rds_default_options" {
  type = object(
    {
      storage_type = string,
      engine = string,
      engine_version = string,
      instance_class = string,
      name = string, # init db name
      identifier = string,
      username = string,
      password = string,
      parameter_group_name = string,
      skip_final_snapshot = bool,
    }
  )
}