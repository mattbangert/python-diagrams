from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3
from diagrams.onprem.compute import Server

with Diagram("XRAY Results API", show=False):
    lb = ELB("lb")
    resultsApi = Lambda("Results API")
    lb >> resultsApi
    resultsApi >> Server("XRAY Cloud") 
    resultsApi >> S3("store")