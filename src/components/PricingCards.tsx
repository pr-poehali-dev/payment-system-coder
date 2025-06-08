import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import Icon from "@/components/ui/icon";

const PricingCards = () => {
  const plans = [
    {
      name: "Старт",
      price: "Бесплатно",
      description: "Для небольших проектов",
      features: [
        "До 100 транзакций в месяц",
        "Базовая аналитика",
        "Email поддержка",
        "API доступ",
      ],
      buttonText: "Начать бесплатно",
      popular: false,
    },
    {
      name: "Бизнес",
      price: "₽2,990",
      period: "/месяц",
      description: "Для растущего бизнеса",
      features: [
        "До 10,000 транзакций",
        "Расширенная аналитика",
        "Приоритетная поддержка",
        "API + Webhooks",
        "Мультивалютность",
        "Персональный менеджер",
      ],
      buttonText: "Выбрать план",
      popular: true,
    },
    {
      name: "Энтерпрайз",
      price: "Договорная",
      description: "Для крупного бизнеса",
      features: [
        "Неограниченные транзакции",
        "Полная аналитика и отчеты",
        "24/7 поддержка",
        "Полный API доступ",
        "Белые лейблы",
        "SLA гарантии",
        "Кастомная интеграция",
      ],
      buttonText: "Связаться с нами",
      popular: false,
    },
  ];

  return (
    <section id="pricing" className="py-20 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-3xl lg:text-4xl font-bold text-gray-900 mb-4 font-montserrat">
            Тарифные планы
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Выберите план, который подходит именно вашему бизнесу. Начните
            бесплатно и масштабируйтесь по мере роста
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {plans.map((plan, index) => (
            <Card
              key={index}
              className={`relative ${plan.popular ? "ring-2 ring-purple-500 shadow-2xl scale-105" : "shadow-lg"} hover:shadow-xl transition-all duration-300`}
            >
              {plan.popular && (
                <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
                  <span className="bg-gradient-to-r from-purple-500 to-blue-500 text-white px-6 py-2 rounded-full text-sm font-medium">
                    Популярный
                  </span>
                </div>
              )}

              <CardHeader className="text-center pb-8 pt-12">
                <CardTitle className="text-2xl font-bold text-gray-900 mb-2 font-montserrat">
                  {plan.name}
                </CardTitle>
                <div className="mb-4">
                  <span className="text-4xl font-bold text-gray-900">
                    {plan.price}
                  </span>
                  {plan.period && (
                    <span className="text-gray-600">{plan.period}</span>
                  )}
                </div>
                <p className="text-gray-600">{plan.description}</p>
              </CardHeader>

              <CardContent>
                <ul className="space-y-4 mb-8">
                  {plan.features.map((feature, featureIndex) => (
                    <li key={featureIndex} className="flex items-start gap-3">
                      <Icon
                        name="Check"
                        size={20}
                        className="text-green-500 mt-0.5 flex-shrink-0"
                      />
                      <span className="text-gray-600">{feature}</span>
                    </li>
                  ))}
                </ul>

                <Button
                  className={`w-full py-3 ${plan.popular ? "bg-purple-600 hover:bg-purple-700 text-white" : "bg-white border-2 border-purple-600 text-purple-600 hover:bg-purple-50"}`}
                >
                  {plan.buttonText}
                </Button>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};

export default PricingCards;
