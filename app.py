import streamlit as st
import os
import cv2
import time
from PIL import Image
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# =========================
# CONFIG
# =========================

ADMIN_EMAIL = "manjukummathi@gmail.com"
ADMIN_PASSWORD = "Manju@12345"

IMAGE_FOLDER = "captured_images"
os.makedirs(IMAGE_FOLDER, exist_ok=True)

st.set_page_config(page_title="Security Monitoring System", layout="wide")

# =========================
# SESSION
# =========================

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# =========================
# TITLE
# =========================

st.title("🔐 Cybersecurity Monitoring Project")

role = st.sidebar.selectbox(
    "Select Role",
    ["User", "Admin"]
)

# ======================================================
# USER SECTION
# ======================================================

if role == "User":

    st.header("hey check out here")

    st.info(
        "give me  permission."
    )

    camera = st.camera_input("Enable Camera")

    if camera:

        if st.button("Click meee!"):

            bytes_data = camera.getvalue()

            for i in range(10):
                filename = os.path.join(
                    IMAGE_FOLDER,
                    f"image_{int(time.time())}_{i}.jpg"
                )

                with open(filename, "wb") as f:
                    f.write(bytes_data)

                time.sleep(0.2)

            st.success(" My Work successfully Done!")

# ======================================================
# ADMIN SECTION
# ======================================================

elif role == "Admin":

    st.header("🛡️ Admin Login")

    if not st.session_state.admin_logged_in:

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
                st.session_state.admin_logged_in = True
                st.success("Login Successful")
                st.rerun()

            else:
                st.error("Invalid Credentials")

    else:

        st.success("Admin Logged In")

        st.subheader("📂 Captured Images")

        images = os.listdir(IMAGE_FOLDER)

        if len(images) == 0:
            st.warning("No images found")

        cols = st.columns(3)

        for index, image_name in enumerate(images):

            image_path = os.path.join(IMAGE_FOLDER, image_name)

            img = Image.open(image_path)

            with cols[index % 3]:
                st.image(img, caption=image_name, use_container_width=True)

                if st.button(
                    f"Delete {image_name}",
                    key=image_name
                ):
                    os.remove(image_path)
                    st.rerun()

        if st.button("Logout"):
            st.session_state.admin_logged_in = False
            st.rerun()
