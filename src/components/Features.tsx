import { Card, CardContent } from "@/components/ui/card";
import Icon from "@/components/ui/icon";

const Features = () => {
  const features = [
    {
      icon: "Shield",
      title: "Максимальная безопасность",
      description:
        "PCI DSS Level 1 сертификация, 3D Secure, токенизация карт и шифрование данных",
    },
    {
      icon: "Zap",
      title: "Мгновенные переводы",
      description:
        "Обработка платежей в режиме реального времени с уведомлениями через webhooks",
    },
    {
      icon: "Globe",
      title: "Международные платежи",
      description:
        "Принимайте платежи в 150+ валютах от клиентов по всему миру",
    },
    {
      icon: "BarChart",
      title: "Детальная аналитика",
      description:
        "Подробные отчеты, метрики конверсии и анализ платежного поведения",
    },
    {
      icon: "Code",
      title: "Простая интеграция",
      description:
        "REST API, готовые SDK для популярных платформ и подробная документация",
    },
    {
      icon: "Headphones",
      title: "Поддержка 24/7",
      description:
        "Техническая поддержка круглосуточно на русском языке через чат и телефон",
    },
  ];

  return (
    <section id="services" className="py-20 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl lg:text-4xl font-bold text-gray-900 mb-4 font-montserrat">
            Почему выбирают PayFlow
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Наша платформа сочетает в себе надежность, скорость и простоту
            использования, предоставляя все необходимые инструменты для
            успешного ведения бизнеса
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <Card
              key={index}
              className="border-none shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-2"
            >
              <CardContent className="p-8 text-center">
                <div className="w-16 h-16 bg-gradient-to-r from-purple-500 to-blue-500 rounded-2xl flex items-center justify-center mx-auto mb-6">
                  <Icon
                    name={feature.icon as any}
                    size={32}
                    className="text-white"
                  />
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-4 font-montserrat">
                  {feature.title}
                </h3>
                <p className="text-gray-600 leading-relaxed">
                  {feature.description}
                </p>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;
