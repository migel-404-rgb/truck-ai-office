import time
import random
import streamlit as st

st.set_page_config(page_title="Truck AI Office Simulation", page_icon="🏢", layout="wide")

st.title("🏢 ออฟฟิศจำลอง: ทีม AI บริหารรถบรรทุก 13 คัน")
st.markdown("จำลองตัวละคร AI แต่ละแผนก (ผู้จัดการ, วางแผน, การตลาด) ที่กำลังเดินทำงานและปรึกษากันในออฟฟิศเสมือนจริง")

if "agents" not in st.session_state:
    st.session_state.agents = {
        "ผู้จัดการ (Manager AI)": {"pos": "โต๊ะกลางออฟฟิศ", "status": "กำลังตรวจภาพรวมรถ 13 คัน", "icon": "👨‍💼", "action": "อนุมัติแผนวิ่งงาน"},
        "ทีมวางแผน (Planner AI)": {"pos": "โต๊ะแผนที่และเส้นทาง", "status": "กำลังคำนวณเส้นทางประหยัดน้ำมัน", "icon": "🗺️", "action": "จัดตารางรถบรรทุก"},
        "ทีมการตลาด (Marketing AI)": {"pos": "โต๊ะเจรจาลูกค้า", "status": "หาเที่ยววิ่งขากลับ (Backhaul)", "icon": "💻", "action": "ดีลงานลูกค้าใหม่"}
    }

if "logs" not in st.session_state:
    st.session_state.logs = ["ระบบเริ่มทำงาน: รถบรรทุกทั้ง 13 คันพร้อมปฏิบัติการ"]

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📍 แผนผังออฟฟิศเสมือนจริง")
    for name, data in st.session_state.agents.items():
        st.markdown(f"""
            <div style="padding: 15px; border-radius: 10px; border: 2px solid #4CAF50; margin-bottom: 10px; background-color: #f9f9f9;">
                <h3>{data['icon']} {name}</h3>
                <p><b>📍 ตำแหน่ง:</b> {data['pos']}</p>
                <p><b>⚡ สถานะปัจจุบัน:</b> <span style="color: green;">{data['status']}</span></p>
                <p><b>⚙️ งานหลัก:</b> {data['action']}</p>
            </div>
        """, unsafe_allow_html=True)

    if st.button("🔄 จำลองเหตุการณ์ถัดไป (ให้ AI เดินและปรึกษากัน)"):
        actions_pool = [
            ("เดินไปคุยกับโต๊ะวางแผน", "กำลังปรึกษาเรื่องเส้นทางภาคเหนือ"),
            ("เดินไปตรวจเช็คโกดัง", "เช็คสภาพความพร้อมรถบรรทุก 13 คัน"),
            ("คุยกับทีมการตลาด", "อัปเดตยอดขนส่งประจำสัปดาห์"),
            ("นั่งประจำโต๊ะ", "กำลังประมวลผลข้อมูล AI Self-Improvement")
        ]
        for name in st.session_state.agents:
            chosen = random.choice(actions_pool)
            st.session_state.agents[name]["pos"] = chosen[0]
            st.session_state.agents[name]["status"] = chosen[1]
        
        new_log = f"[{time.strftime('%H:%M:%S')}] AI ทั้ง 3 แผนกมีการอัปเดตสถานะและแชร์ข้อมูลกันเรียบร้อย"
        st.session_state.logs.insert(0, new_log)
        st.rerun()

with col2:
    st.subheader("💬 บันทึกการสนทนาของ AI (Logs)")
    for log in st.session_state.logs[:10]:
        st.info(log)

st.divider()
st.subheader("🚚 สถานะกองรถบรรทุก 13 คันในระบบ")
cols = st.columns(4)
for i in range(1, 14):
    with cols[(i-1) % 4]:
        status_choice = random.choice(["🟢 วิ่งส่งสินค้า", "🔵 รอรับงานขากลับ", "🟡 จอดพักตรวจเช็ค"])
        st.metric(label=f"รถบรรทุกคันที่ {i:02d}", value=status_choice)