################## D E C L A R E - V A R I A B L E ####################

################################### A W S #################################

variable "access_key" {}
variable "secret_key" {}
variable "region" {}

################################### V P C #################################
variable "vpc_id" {}
variable "aws_vpc" {}
variable "cidr_block" {}

################################### S U B N E T # 1 #################################

variable "subnet1_id" {}
variable "availability_zone_1" {}
variable "availability_zone_2" {}
variable "subnet_1_cidr_block" {}


################################### S U B N E T # 2 #################################

variable "subnet2_id" {}
variable "subnet_2_cidr_block" {}

###################### I N T E R N E T - G A T E W A Y #################################

variable "aws_internet_gateway" {}

###################### R O U T E - T A B L E #################################

variable "aws_default_route_table" {}

################################### I N S T A N C E S #################################

variable "ami" {}
variable "instance_type" {}

variable "key_name" {}

variable "ud_pyhon" {
  description = "path to python script"
  default     = "userdata_py.sh"
}
variable "ud_jenkins" {
  description = "path to jenkins with python script"
  default     = "userdata_jenkins.sh"
}


####################### S E C U R I T Y - G R O U P # 1 ##############################
variable "vpc_security_group_ids" {}
variable "aws_security_group" {}
variable "aws_security_group_ids" {}

####################### S E C U R I T Y - G R O U P # 2 ##############################
