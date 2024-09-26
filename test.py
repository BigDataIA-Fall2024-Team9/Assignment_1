# !pip install diagrams

from diagrams import Cluster, Diagram
from diagrams.gcp.compute import GCE
from diagrams.gcp.storage import GCS
from diagrams.gcp.storage import GCS as ObjectStorage
from diagrams.gcp.database import SQL
from diagrams.custom import Custom
from diagrams.onprem.client import Users  # Import Users icon

#diagram
with Diagram("Hugging Face Dataset to OpenAI via Streamlit", show=True):
    
    # Hugging Face Dataset
    huggingface = Custom("Hugging Face Dataset", "./hugging_face.png", width="3.0", height="2.0") 
    # Python (Using a custom logo for EDA)
    EDA = Custom("EDA", "./EDA_logo.png")  # Path to EDA logo
    # GCP Cloud Services
    with Cluster("Google Cloud Platform"):
        gcs = GCS("Google Cloud Storage")
        gce = GCE("Google Compute Engine")       
        # Object Storage and SQL inside GCP
        object_storage = ObjectStorage("Object Storage")
        rdbms = SQL("RDBMS")

    # Streamlit
    streamlit = Custom("Streamlit App", "./streamlit_logo.png")
    # OpenAI
    openai = Custom("OpenAI Model", "./openai_logo.png")  
    # Users
    users = Users("Users")
    # Define the architecture connections
    huggingface >> EDA >> gcs >> gce >> streamlit >> openai 
    openai >> streamlit  #connection from OpenAI to Streamlit
    openai >> streamlit  #connection from OpenAI to Streamlit
    users >> streamlit  # Users sending requests to Streamlit
    streamlit >> users  # Streamlit sending responses back to users
    # Streamlit sending data back to GCP
    streamlit >> gce  # Streamlit communicating back with GCP(Google Compute Engine)
    # GCP interacting with Object Storage and RDBMS in both directions
    gce >> object_storage  # GCP communicating with Object Storage
    object_storage >> gce  # Object Storage sending data to GCP
    gce >> rdbms  # GCP communicating with SQL
    rdbms >> gce  # SQL sending data back to GCP 
