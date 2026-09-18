import time
import random
import streamlit as st

st.set_page_config(page_title="Pixel AI Office Simulation", page_icon="🕹️", layout="wide")

DIESEL_PRICE = 40.69  # ราคาน้ำมันดีเซลปัจจุบัน

st.title("🕹️ เกมจำลองออฟฟิศ AI: บริหารกองรถบรรทุก 13 คัน")
st.markdown("ระบบจำลองตัวละครเดินในออฟฟิศ ปรึกษากัน และตัดสินใจ **รับสมัคร/ปลดพนักงาน** อัตโนมัติด้วย AI")

# กำหนดสถานะตัวละครและพนักงานในบริษัท
if "office_staff" not in st.session_state:
    st.session_state.office_staff = [
        {"name": "Manager AI (สมชาย)", "role": "ผู้จัดการ", "pos": "โต๊ะกลาง (Manager Desk)", "status": "กำลังตรวจบัญชีรวม", "icon": "👨‍💼", "perf": 85},
        {"name": "Planner AI (สมศักดิ์)", "role": "ทีมวางแผนเส้นทาง", "pos": "โต๊ะแผนที่ (Map Desk)", "status": f"คุมค่าน้ำมัน ({DIESEL_PRICE}บ.)", "icon": "🗺️", "perf": 78},
        {"name": "Marketing AI (มีנה)", "role": "ทีมการตลาด", "pos": "โต๊ะลูกค้า (Sales Desk)", "status": "หาเที่ยววิ่งขากลับ", "icon": "💻", "perf": 90},
        {"name": "Driver 01 (พี่กบ)", "role": "คนขับรถบรรทุก", "pos": "ลานจอดรถ", "status": "วิ่งงาน กทม.-เชียงใหม่", "icon": "🚚", "perf": 65},
        {"name": "Driver 02 (น้าชาติ)", "role": "คนขับรถบรรทุก", "pos": "ลานจอดรถ", "status": "รอรับงาน", "icon": "🚚", "perf": 45}, # กำลังจะโดนเพ่งเล็ง
    ]

if "office_logs" not in st.session_state:
    st.session_state.office_logs = [
        "[08:00] เปิดออฟฟิศจำลอง: AI เริ่มเข้าประจำตำแหน่งเพื่อบริหารรถ 13 คัน"
    ]

# แบ่งหน้าจอจำลองแผนผังออฟฟิศ (ซ้าย) กับ ห้องสนทนา/ระบบ HR (ขวา)
col_map, col_chat = st.columns([1.5, 1])

with col_map:
    st.subheader("🗺️ แผนผังห้องทำงาน (Office Floor)")
    
    # จำลองหน้าจอแบบ Pixel / Game Grid ด้วย HTML สวยๆ
    grid_html = """
    <div style="background-color: #2e4053; padding: 20px; border-radius: 12px; color: white; font-family: monospace;">
        <h4 style="margin-top:0; color: #f1c40f;">🏢 [โซนห้องทำงานรวม AI & กองรถ 13 คัน]</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    """
    
    for staff in st.session_state.office_staff:
        grid_html += f"""
            <div style="background: #34495e; padding: 10px; border-radius: 8px; border-left: 5px solid #3498db;">
                <b>{staff['icon']} {staff['name']}</b><br>
                <span style="font-size: 12px; color: #bdc3c7;">📍 {staff['pos']}</span><br>
                <span style="font-size: 12px; color: #2ecc71;">⚡ {staff['status']}</span><br>
                <span style="font-size: 11px; color: #e74c3c;">📊 ประสิทธิภาพ: {staff['perf']}%</span>
            </div>
        """
    grid_html += "</div></div>"
    st.markdown(grid_html, unsafe_allow_html=True)
    
    st.write("")
    if st.button("▶️ กดให้ตัวละครเดินคุยกัน & ประเมินผลงาน (AI Action)"):
        # สุ่มให้ตัวละครเดินเปลี่ยนตำแหน่งและคุยกัน
        actions_pool = [
            ("เดินไปปรึกษาโต๊ะวางแผน", "กำลังถกเรื่องราคาน้ำมันแพงขึ้น"),
            ("เดินไปตรวจโกดังรถ 13 คัน", "เช็คสภาพยางและไมล์รถบรรทุก"),
            ("เดินไปชงกาแฟคุยกับแผนกการตลาด", "อัปเดตยอดลูกค้าจองรถขากลับ"),
            ("นั่งประจำโต๊ะวิเคราะห์ข้อมูล", "ประเมินผลกำไรสุทธิรายวัน")
        ]
        
        for staff in st.session_state.office_staff:
            if "Driver" not in staff['name']:
                chosen = random.choice(actions_pool)
                staff['pos'] = chosen[0]
                staff['status'] = chosen[1]
                staff['perf'] = min(100, max(30, staff['perf'] + random.randint(-5, 5)))

        # ระบบ AI ตัดสินใจรับคนเพิ่ม หรือ ไล่คนออกเองอัตโนมัติ
        event_chance = random.random()
        if event_chance > 0.5 and len(st.session_state.office_staff) < 8:
            # รับสมัครพนักงานเพิ่มเอง
            new_id = len(st.session_state.office_staff) + 1
            new_name = f"Driver {new_id:02d} (เด็กใหม่)"
            st.session_state.office_staff.append({
                "name": new_name, "role": "คนขับรถบรรทุก", "pos": "ลานจอดรถ", "status": "พร้อมเริ่มงาน", "icon": "🚚", "perf": 80
            })
            st.session_state.office_logs.insert(0, f"🤖 [Manager AI ตัดสินใจรับสมัคร]: รับ '{new_name}' เข้าทำงาน เนื่องจากงานขนส่งรถ 13 คันล้นมือและต้องการเพิ่มเที่ยววิ่ง")
        
        elif event_chance <= 0.5:
            # ตรวจสอบหาพนักงานที่ประสิทธิภาพต่ำกว่า 50 เพื่อไล่ออก
            low_performers = [s for s in st.session_state.office_staff if s['perf'] < 50 and "Driver" in s['name']]
            if low_performers:
                fired = low_performers[0]
                st.session_state.office_staff.remove(fired)
                st.session_state.office_logs.insert(0, f"🔥 [Manager AI ตัดสินใจปลดพนักงาน]: ไล่ '{fired['name']}' ออก! เนื่องจากคะแนนประสิทธิภาพเหลือเพียง {fired['perf']}% และใช้น้ำมันเกินโควตา")
            else:
                st.session_state.office_logs.insert(0, f"💬 [AI Chat]: ทีมวางแผนบอกผู้จัดการว่า 'ราคาน้ำมันดีเซล {DIESEL_PRICE} บาท ทำให้ต้องคัดเลือกเส้นทางสั้นที่คุ้มกำไรที่สุด'")

        st.rerun()

with col_chat:
    st.subheader("💬 บันทึกการสนทนา & ระบบ HR (AI Logs)")
    chat_box = st.container()
    with chat_box:
        for log in st.session_state.office_logs[:10]:
            st.info(log)

st.divider()
st.subheader("🚚 สรุปสถานะกองรถบรรทุก 13 คัน & ต้นทุนปัจจุบัน")
c1, c2, c3 = st.columns(3)
c1.metric("กองรถทั้งหมด", "13 คัน", "พร้อมวิ่ง 11 คัน")
c2.metric("ราคาน้ำมันดีเซล", f"{DIESEL_PRICE} ฿/ลิตร", "อ้างอิงปัจจุบัน")
c3.metric("พนักงานในออฟฟิศ", f"{len(st.session_state.office_staff)} คน", "จัดการโดย AI อัตโนมัติ")
