import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TradeButtonComponent } from './trade-button.component';

describe('TradeButtonComponent', () => {
  let component: TradeButtonComponent;
  let fixture: ComponentFixture<TradeButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TradeButtonComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TradeButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
