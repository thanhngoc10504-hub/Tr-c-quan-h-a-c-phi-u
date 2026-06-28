ax[1].grid(True)
st.image("logo.jpg.jfif")
    plt.tight_layout()

    st.pyplot(fig)

    # =============================
    # BIỂU ĐỒ NẾN
    # =============================
    st.subheader("🕯️ Biểu đồ nến")

    fig2, _ = mpf.plot(
        df,
        type="candle",
        mav=(10, 20),
        volume=True,
        style="yahoo",
        figsize=(12, 6),
        title=ticker,
        returnfig=True
    )

    st.pyplot(fig2)

    # =============================
    # KIỂM ĐỊNH MANN-KENDALL
    # =============================
    close_prices = df["Close"].dropna().reset_index(drop=True)

    result = mk.original_test(close_prices)

    st.subheader("📊 Kết quả kiểm định Mann-Kendall")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Trend", result.trend)
        st.metric("Tau", f"{result.Tau:.4f}")

    with col2:
        st.metric("p-value", f"{result.p:.6f}")
        st.metric("Variance S", f"{result.var_s:.2f}")

    st.markdown("---")

    if result.p < 0.05:
        if result.trend == "increasing":
            st.success("Có xu hướng **TĂNG** có ý nghĩa thống kê (p < 0.05).")
        elif result.trend == "decreasing":
            st.success("Có xu hướng **GIẢM** có ý nghĩa thống kê (p < 0.05).")
        else:
            st.success("Có xu hướng đáng kể về mặt thống kê.")
    else:
        st.warning("Không phát hiện xu hướng có ý nghĩa thống kê (p ≥ 0.05).")
