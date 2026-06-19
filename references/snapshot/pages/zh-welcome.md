<!-- title: Stepfun 开放平台文档中心 -->
<!-- source: https://platform.stepfun.com/docs/zh/welcome.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Stepfun 开放平台文档中心

export const heroSlides = [{
  title: "全新 Step Plan",
  desc: "升级 Credit 月池，加油包随时补 · 按需选档的订阅制 AI 服务",
  href: "/zh/step-plan/overview",
  cta: "查看套餐"
}, {
  title: "Step 3.7 Flash",
  desc: "面向 Agent / Coding / 多模态工作流的高效率 Flash 旗舰",
  href: "/zh/guides/models/step-3.7-flash",
  cta: "查看模型"
}, {
  title: "StepAudio 2.5 Realtime",
  desc: "活人感实时语音大模型，懂副语言、自定义人设",
  href: "/zh/guides/models/stepaudio-2.5-realtime",
  cta: "查看模型"
}, {
  title: "StepAudio 2.5 Chat",
  desc: "活人感对话大模型，文本返回，自定义人设",
  href: "/zh/guides/models/stepaudio-2.5-chat",
  cta: "查看模型"
}, {
  title: "Step Image Edit 2",
  desc: "文生图与图像编辑一体化模型",
  href: "/zh/guides/models/step-image-edit-2",
  cta: "查看模型"
}];

export const quickStartItems = [{
  key: "quickstart",
  title: "快速开始",
  desc: "5 分钟完成首次 API 调用",
  href: "/zh/quickstart/overview"
}, {
  key: "console",
  title: "控制台",
  desc: "管理 API Key，查看用量",
  href: "https://platform.stepfun.com/account-overview"
}, {
  key: "api",
  title: "API 文档",
  desc: "查看接口规范与参数说明",
  href: "/zh/api-reference"
}, {
  key: "coding",
  title: "AI Coding 工具配置",
  desc: "在 AI 编程工具中接入 Step 系列模型",
  href: "/zh/step-plan/quick-start"
}, {
  key: "pricing",
  title: "定价与计费",
  desc: "查看模型价格与流控配额",
  href: "/zh/guides/pricing"
}, {
  key: "faq",
  title: "常见问题",
  desc: "查询常见疑问与答疑",
  href: "/zh/faq/common-questions"
}];

export const HeroCarousel = () => {
  const total = heroSlides.length;
  const [i, setI] = useState(0);
  useEffect(() => {
    const heroEl = document.querySelector(".sf-hero");
    if (!heroEl) return;
    const touched = [];
    let n = heroEl;
    while (n && n !== document.body) {
      const px = parseInt(getComputedStyle(n).maxWidth);
      if (px >= 1100 && px <= 1500) {
        n.style.maxWidth = "none";
        touched.push(n);
      }
      n = n.parentElement;
    }
    return () => touched.forEach(el => el.style.maxWidth = "");
  }, []);
  useEffect(() => {
    const t = setTimeout(() => setI(p => (p + 1) % total), 5000);
    return () => clearTimeout(t);
  }, [total, i]);
  return <section className="sf-hero sf-hero--orn-grid">
      <button type="button" className="sf-hero__arrow sf-hero__arrow--prev" aria-label="上一张" onClick={() => setI(p => (p - 1 + total) % total)}>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
          <path d="M15 18l-6-6 6-6" />
        </svg>
      </button>
      <button type="button" className="sf-hero__arrow sf-hero__arrow--next" aria-label="下一张" onClick={() => setI(p => (p + 1) % total)}>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
          <path d="M9 6l6 6-6 6" />
        </svg>
      </button>
      <div className="sf-hero__viewport">
        <div className="sf-hero__track" style={{
    width: `${total * 100}%`,
    transform: `translateX(-${i * (100 / total)}%)`,
    transition: "transform 0.55s cubic-bezier(0.65, 0.05, 0.36, 1)"
  }}>
          {heroSlides.map(s => <div className="sf-hero__slide" key={s.title} style={{
    flex: `0 0 ${100 / total}%`
  }}>
              <h2 className="sf-hero__title">{s.title}</h2>
              {s.desc ? <p className="sf-hero__desc">{s.desc}</p> : null}
              {s.href ? <a className="sf-hero__cta" href={s.href}>
                  <span>{s.cta || "查看详情"}</span>
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
                    <path d="M5 12h14M13 5l7 7-7 7" />
                  </svg>
                </a> : null}
            </div>)}
        </div>
      </div>
      <div className="sf-hero__dots" role="tablist" aria-label="banner 进度">
        {heroSlides.map((s, idx) => <button key={s.title} type="button" role="tab" aria-selected={idx === i} aria-label={`第 ${idx + 1} 张`} className={`sf-hero__dot${idx === i ? " is-on" : ""}`} onClick={() => setI(idx)} />)}
      </div>
    </section>;
};

<HeroCarousel />

<div className="sf-qcards-wrap">
  <div className="sf-qcards-head">
    <h3>快捷入口</h3>
  </div>

  <div className="sf-qcards">
    {quickStartItems.map((it) => (
            <a className="sf-qcard" href={it.href} key={it.title}>
              <div className="sf-qcard__icon">
                {it.key === "quickstart" && (
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
                    <path d="m13 2-3 7h7l-9 13 3-9H4z" />
                  </svg>
                )}
                {it.key === "console" && (
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
                    <rect x="3" y="3" width="7" height="7" rx="1" />
                    <rect x="14" y="3" width="7" height="7" rx="1" />
                    <rect x="3" y="14" width="7" height="7" rx="1" />
                    <rect x="14" y="14" width="7" height="7" rx="1" />
                  </svg>
                )}
                {it.key === "api" && (
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
                    <circle cx="12" cy="12" r="3" />
                    <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z" />
                  </svg>
                )}
                {it.key === "coding" && (
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
                    <polyline points="16 18 22 12 16 6" />
                    <polyline points="8 6 2 12 8 18" />
                  </svg>
                )}
                {it.key === "pricing" && (
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
                    <circle cx="12" cy="12" r="9" />
                    <path d="M12 7v5l3 2" />
                  </svg>
                )}
                {it.key === "faq" && (
                  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
                    <circle cx="12" cy="12" r="9" />
                    <path d="M9.1 9a3 3 0 1 1 5.8 1c0 2-3 3-3 3" />
                    <path d="M12 17h.01" />
                  </svg>
                )}
              </div>
              <h4>{it.title}</h4>
              <p>{it.desc}</p>
            </a>
          ))}
  </div>
</div>
