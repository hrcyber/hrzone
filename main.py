import streamlit as st

# Set the page configuration
st.set_page_config(page_title="HR CYBER ZONE", page_icon="🛠", layout="wide")

# Title and Header
st.title("HR CYBER ZONE")
st.subheader("Your One-Stop Solution for Software Development and CCTV Services")

# Description
st.markdown(
    """
    Welcome to **HR CYBER ZONE**! We offer a range of services:
    - **Software Development**: Tailored software solutions for your business.
    - **User Orders**: Custom orders for your software needs.
    - **CCTV Sales and Services**: High-quality CCTV cameras and reliable services.

    Our team is dedicated to providing top-notch solutions for all your technological needs.
    """
)

# Services Section
st.header("Our Services")

col1, col2 = st.columns(2)

with col1:
    st.image("https://via.placeholder.com/400", caption="Software Development", use_column_width=True)
    st.markdown(
        """
        ### Software Development
        - Custom software solutions
        - Mobile and web app development
        - Maintenance and support
        """
    )

with col2:
    st.image("https://via.placeholder.com/400", caption="CCTV Services", use_column_width=True)
    st.markdown(
        """
        ### CCTV Sales and Services
        - High-quality CCTV cameras
        - Installation and maintenance
        - 24/7 support
        """
    )

# Order Section
st.header("Place an Order")
st.markdown("We'd love to hear from you! Please fill out the form below to place an order.")

with st.form("order_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    service = st.selectbox("Select a Service", ["Software Development", "CCTV Sales", "CCTV Service"])
    details = st.text_area("Order Details", placeholder="Provide more information about your requirements")
    submitted = st.form_submit_button("Submit Order")

    if submitted:
        st.success(
            f"Thank you, {name}! Your order for {service} has been received. We will contact you at {email} shortly.")

# Contact Information
st.header("Contact Us")
st.markdown(
    """
    **Address**: Near Petrol Pump , Ara saram road, Piro 
    **Phone**: tel:7739351021 7870818473

    Follow us for updates and offers!
    """
)

# Footer
st.markdown(
    """
    ---

    © 2024 HR CYBER ZONE. All rights reserved.
    """
)
