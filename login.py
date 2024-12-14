import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Đường dẫn đến msedgedriver
driver_path = "C:/Users/maxgy/Downloads/edgedriver_win64/msedgedriver.exe"
# Khởi tạo đối tượng Service cho Edge
service = Service(driver_path)

# Khởi tạo đối tượng WebDriver cho Microsoft Edge
driver = webdriver.Edge(service=service)

try:
    # Truy cập trang đăng nhập
    driver.get("https://worksuite.cloodo.com/login")  # Thay đổi URL với trang web của bạn

    # Đợi trang tải xong và tìm phần tử email
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

    # Tìm các phần tử đăng nhập
    username_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")  # Cập nhật theo trang của bạn
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

    # Điền thông tin đăng nhập và nhấn nút login
    username_field.send_keys("")  # Thay đổi với tên người dùng của bạn
    time.sleep(3)
    password_field.send_keys("")  # Thay đổi với mật khẩu của bạn
    time.sleep(3)
    login_button.click()
    time.sleep(4)
    # Đợi trang tải xong sau khi nhấn đăng nhập
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "welcome_message")))

    # Kiểm tra xem đăng nhập có thành công hay không
    try:
        welcome_message = driver.find_element(By.ID, "welcome_message")
        if welcome_message.is_displayed():
            print("Đăng nhập thành công!")
        else:
            print("Đăng nhập không thành công.")
    except NoSuchElementException:
        print("Không thể tìm thấy phần tử xác nhận đăng nhập thành công.")
        print("Lỗi: Phần tử xác nhận đăng nhập không tồn tại.")

except NoSuchElementException as e:
    print(f"Lỗi khi tìm phần tử: {e}")
except TimeoutException as e:
    print(f"Lỗi thời gian chờ: {e}")
except Exception as e:
    print(f"Lỗi không xác định: {e}")
finally:
    driver.quit()  # Đảm bảo đóng trình duyệt khi hoàn thành
